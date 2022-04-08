import json
import os
import re
import urllib.request

import boto3

# Boto3 Clients
s3 = boto3.resource('s3')
s3client = boto3.client('s3')
comprehend = boto3.client('comprehend')
firehose = boto3.client('firehose')
rekognition = boto3.client('rekognition')

# Global Vars
sentiment_stream = os.environ['SENTIMENT_STREAM']
entity_stream = os.environ['ENTITY_STREAM']
rekognition_stream = os.environ['REKOGNITION_STREAM']
s3_bucket = os.environ['BUCKET']
imagekey_prefix = os.environ['IMAGEKEY_PREFIX']


def label_image(image_url):
    # Extract image path from media_url
    image_reg = r".*\/(?P<mediahash>[^\.]*)\.(?P<ext>[^\.]{3})"
    image_match = re.match(image_reg, image_url)
    image_path = image_match.group('mediahash') + '.' + image_match.group('ext')
    image_fullpath = '/tmp/' + image_path

    # Catch unsupported extensions
    if not image_match.group('ext') in ('jpg', 'png'):
        return (None, None)
    image_s3_key = imagekey_prefix + image_path

    # Logic to prevent rework
    bucket = s3.Bucket(s3_bucket)

    objs = list(bucket.objects.filter(Prefix=image_s3_key))
    if len(objs) == 0:
        # Download Image
        try:
            urllib.request.urlretrieve(image_url, image_fullpath)
        except Exception as e:
            print('Failed to analyze image: {image} {error}'.format(image=image_url, error=str(e)))
            return (None, None)
        # Upload Image to S3
        s3client.upload_file(image_fullpath, s3_bucket, image_s3_key)
        # Remove Local Copy of Image
        os.remove(image_fullpath)

    # Rekognition API Parameters
    image = {
        'S3Object': {
            'Bucket': s3_bucket,
            'Name': image_s3_key
        }
    }

    try:
        # Detect Labels
        labels = rekognition.detect_labels(Image=image,
                                           MaxLabels=100,
                                           MinConfidence=50.0)

        # Detect Moderation Labels
        moderation = rekognition.detect_moderation_labels(Image=image)

        # Construct Empty Objects for when APIs are not run
        text = {
            'TextDetections': []
        }
        celebrities = {
            'UnrecognizedFaces': [],
            'CelebrityFaces': [],
            'OrientationCorrection': 'ROTATE_0'
        }
        faces = {
            'FaceDetails': []
        }

        # Determine the need to run Detect Text, Recognize Celebrities, or Detect Faces APIs based on labels detected in image
        labelNames = {label['Name'] for label in labels['Labels']}

        if 'Text' in labelNames:
            # Detect Text
            text = rekognition.detect_text(Image=image)

        if 'Person' in labelNames:
            # Detect Celebrities
            celebrities = rekognition.recognize_celebrities(Image=image)
            # Detect Faces
            faces = rekognition.detect_faces(Image=image, Attributes=['ALL'])
        item = {
            'Labels': labels['Labels'],
            'TextDetections': text['TextDetections'],
            'CelebrityRecognition': {
                'UnrecognizedFaces': celebrities['UnrecognizedFaces'],
                'CelebrityFaces': celebrities['CelebrityFaces'],
                'OrientationCorrection': celebrities['OrientationCorrection']
            },
            'FaceDetails': faces['FaceDetails'],
            'ModerationLabels': moderation['ModerationLabels']
        }
        print('Processed: s3://{bucket}/{key}'.format(bucket=s3_bucket, key=image_s3_key))
        return (item, 's3://{bucket}/{key}'.format(bucket=s3_bucket, key=image_s3_key))
    except Exception as e:
        print('Failed to analyze image: {image} {error}'.format(image=json.dumps(image), error=str(e)))
        return (None, None)


def analyze_tweet(tweet_json):
    tweet = json.loads(tweet_json)

    # Comprehend API Parameters
    tweet_text = tweet['text']
    language_code = 'en'

    # Comprehend Sentiment Detection
    sentiment = comprehend.detect_sentiment(Text=tweet_text, LanguageCode=language_code)
    # If valid response pass to firehose
    if sentiment['ResponseMetadata']['HTTPStatusCode'] == 200:
        sentiment_record = {
            'tweetid': tweet['id'], 'text': tweet_text,
            'sentiment': sentiment['Sentiment'],
            'sentimentPosScore': sentiment['SentimentScore']['Positive'],
            'sentimentNegScore': sentiment['SentimentScore']['Negative'],
            'sentimentNeuScore': sentiment['SentimentScore']['Neutral'],
            'sentimentMixedScore': sentiment['SentimentScore']['Mixed']
        }
        firehose.put_record(DeliveryStreamName=sentiment_stream, Record={'Data': json.dumps(sentiment_record) + '\n'})

    # Comprehend Entity Detection
    entities = comprehend.detect_entities(Text=tweet_text, LanguageCode=language_code)
    # If valid response pass to firehose
    if entities['ResponseMetadata']['HTTPStatusCode'] == 200:
        for entity in entities['Entities']:
            entity_record = {
                'tweetid': tweet['id'],
                'text': tweet_text,
                'entity': entity['Text'],
                'type': entity['Type'],
                'score': entity['Score']
            }
            firehose.put_record(DeliveryStreamName=entity_stream, Record={'Data': json.dumps(entity_record) + '\n'})

    # Use Amazon Rekognition to analyze images in the tweet
    if tweet.get('extended_entities'):
        for media in tweet['extended_entities']['media']:
            if media['type'] == 'photo':
                image_labels, s3image = label_image(media['media_url'])
                if image_labels is not None and len(image_labels) > 0:
                    image_rekognition_record = {
                        'tweetid': tweet['id'],
                        'text': tweet_text,
                        'mediaid': media['id'],
                        'media_url': media['media_url'],
                        'image_labels': image_labels
                    }
                    firehose.put_record(DeliveryStreamName=rekognition_stream,
                                        Record={'Data': json.dumps(image_rekognition_record) + '\n'})


def lambda_handler(event, context):
    # Download tweets from S3, analyze them using Amazon Comprehend and Amazon Rekognition, and send the results to Firehose
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    tweets_file = '/tmp/tweets.json'
    s3client.download_file(bucket, key, tweets_file)
    with open(tweets_file) as f:
        for tweet_json in f:
            analyze_tweet(tweet_json)
