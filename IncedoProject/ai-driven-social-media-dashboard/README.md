# AI-Driven Social Media Dashboard

Voice of customer analytics through social media: Build a social media dashboard using artificial intelligence and
business intelligence services.

Organizations want to understand how customers perceive them and who those customers are. For example, what factors are
driving the most positive and negative experiences for their offerings? Social media interactions between organizations
and customers are a great way to evaluate this and deepen brand awareness. Understanding these conversations are a
low-cost way to acquire leads, improve website traffic, develop customer relationships, and improve customer service.
Since these conversations are all in unstructured text format, it is difficult to scale the analysis and get the full
picture.

## OS/Python Environment Setup

```bash
sudo apt-get update
sudo apt-get install zip sed wget -y
```

## Building Lambda Package

```bash
cd deployment 
./build-s3-dist.sh source-bucket-base-name version
```
e.g.
Create a s3 bucket with name: ai-social-media-dashboard
version: v1.0

Assign the same bucket name and version at the time of creating stack in the cloudformation.

source-bucket-base-name should be the base name for the S3 bucket location where the template will source the Lambda
code from. The template will append '-[region_name]' to this value. version should be a version S3 key prefix For
example: ./build-s3-dist.sh solutions v1.0 The template will then expect the source code to be located in the
solutions-[region_name]/ai-driven-social-media-dashboard/v1.0/

## CF template and Lambda function

Located in deployment/dist

***