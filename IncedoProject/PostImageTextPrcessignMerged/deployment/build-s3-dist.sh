#!/bin/bash

# This assumes all of the OS-level configuration has been completed and git repo has already been cloned
#sudo yum-config-manager --enable epel
#sudo yum update -y
#sudo pip install --upgrade pip
#alias sudo='sudo env PATH=$PATH'
#sudo  pip install --upgrade setuptools
#sudo pip install --upgrade virtualenv

# This script should be run from the repo's deployment directory
# cd deployment
# ./build-s3-dist.sh source-bucket-base-name
# source-bucket-base-name should be the base name for the S3 bucket location where the template will source the Lambda code from.
# The template will append '-[region_name]' to this bucket name.
# For example: ./build-s3-dist.sh solutions
# The template will then expect the source code to be located in the solutions-[region_name] bucket

# Check to see if input has been provided:
if [ -z "$2" ]; then
    echo "Please provide the base source bucket name and version where the lambda code will eventually reside."
    echo "For example: ./build-s3-dist.sh solutions v1.0"
    exit 1
fi

# Build source
echo "Staring to build distribution"
# Create variable for deployment directory to use as a reference for builds
echo "export deployment_dir=`pwd`"
# shellcheck disable=SC2155
export deployment_dir=`pwd`

# Make deployment/dist folder for containing the built solution
echo "mkdir -p $deployment_dir/dist"
mkdir -p $deployment_dir/dist

# Copy project CFN template(s) to "dist" folder and replace bucket name with arg $1
echo "cp -f EyeOfCustomerV1.yaml $deployment_dir/dist/EyeOfCustomerV1.yaml"
cp -f EyeOfCustomerV1.yaml $deployment_dir/dist/EyeOfCustomerV1.yaml
#echo "Updating code source bucket in yaml with $1"
#bucket="s/%%BUCKET_NAME%%/$1/g"
#echo "sed -i '' -e $bucket $deployment_dir/dist/ai-driven-social-media-dashboard.yaml"
#sed -i '' -e $bucket $deployment_dir/dist/ai-driven-social-media-dashboard.yaml
#echo "Updating code source version in yaml with $1"
#version="s/%%VERSION%%/$2/g"
#echo "sed -i '' -e $version $deployment_dir/dist/ai-driven-social-media-dashboard.yaml"
#sed -i '' -e $version $deployment_dir/dist/ai-driven-social-media-dashboard.yaml

# for just getting the raw data od the parameters.
# bucket = "$1"
# version = "$2"

# Package socialmediafunction Lambda function
echo "Packaging socialmediafunction lambda"
cd $deployment_dir/../source/socialmediafunction/ || exit
zip -q -r9 $deployment_dir/dist/socialmediafunction.zip *

# Package addtriggerfunction Lambda function
echo "Packaging addtriggerfunction lambda"
cd $deployment_dir/../source/addtriggerfunction/ || exit
zip -q -r9 $deployment_dir/dist/addtriggerfunction.zip *

# Package labelimage Lambda function
echo "Packaging labelimage lambda function"
cd $deployment_dir/../source/labelimage/ || exit
zip -q -r9 $deployment_dir/dist/labelimage.zip *



#zipping code for ec2, code already provided in s3 bucket
#echo "tarring ec2 twitter reader code"
#cd $deployment_dir/../source/SocialAnalyticsReader/ || exit
# npm install
# npm run build
# npm run tar
# # Copy packaged Lambda function to $deployment_dir/dist

#zip -q -r9 $deployment_dir/dist/ec2_twitter_reader.zip *
#cp ./dist/ec2_twitter_reader.tar $deployment_dir/dist/ec2_twitter_reader.zip
# Remove temporary build files
#rm -rf dist
#rm -rf node_modules

# Done, so go back to deployment_dir
cd $deployment_dir || exit


#aws s3api wait bucket-exists --bucket $1
echo " creating bucket " $1 " in region_name us-east-1 as default"
aws s3api create-bucket --bucket $1 --region us-east-1

aws s3 cp $deployment_dir/dist/socialmediafunction.zip s3://$1/$2/socialmediafunction.zip
aws s3api put-object-acl --bucket $1 --key $2/socialmediafunction.zip --acl public-read # makes the uploaded file public

aws s3 cp $deployment_dir/dist/addtriggerfunction.zip s3://$1/$2/addtriggerfunction.zip
aws s3api put-object-acl --bucket $1 --key $2/addtriggerfunction.zip --acl public-read # makes the uploaded file public

aws s3 cp $deployment_dir/dist/addtriggerfunction.zip s3://$1/$2/labelimage.zip
aws s3api put-object-acl --bucket $1 --key $2/addtriggerfunction.zip --acl public-read # makes the uploaded file public

#aws s3 cp $deployment_dir/dist/ec2_twitter_reader.zip s3://$1/$2/ec2_twitter_reader.zip
#aws s3api put-object-acl --bucket $1 --key $2/ec2_twitter_reader.zip --acl public-read # makes the uploaded file public

aws s3 cp $deployment_dir/dist/EyeOfCustomerV1.yaml s3://$1/$2/EyeOfCustomerV1.yaml
aws s3api put-object-acl --bucket $1 --key $2/EyeOfCustomerV1.yaml --acl public-read # makes the uploaded file public

echo "removing all files from dist"
rm -rf $deployment_dir/dist