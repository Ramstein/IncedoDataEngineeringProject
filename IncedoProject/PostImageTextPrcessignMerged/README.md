# AI-Driven Social Media Dashboard

# IncedoDataEngineeringProject
Enabling More Targeted Promotions and Lower Customer Acquisition Costs using Data Engineering and AI-Incedo

One of Incedo Inc banking and financial services(BFSI) customer wanted to improve their marketing campaigns in order to boost conversion rates while lowering customer acquisition costs. To better target clients and promote the most appropriate products and services, the bank sought to identify channels, offers, and approaches.

The bank decided to collate, aggregate, and analyze a large amount of structured and unstructured data to help identify key indications of interest, including:

- Customer purchase and transaction history
- Customer profile data
- Customer behavior on social media (Twitter, Facebook)

## Data Schema:
- Customer purchase and transaction history
customerNumber (CIF),cardLast4Digits,transactionDate,transactionTime,transactionAmount,transactionType,merchantName,merchantCity,merchantState,merchantZip,stateCode
- Customer profile data
customerNumber (CIF),dateOfBirth,branchNumber,citizenshipCode,currCountryCode,employmentStatus,incomeInThousands,marketSegment,maritalStatus,stateCode,City,customerOpeningDate,Gender

- Social Media: Twitter
Twitter Data Dictionary
Twitter Data Entities
- Social Media: Facebook APIs, SDKs & Guides - Facebook Developer Docs

## TASK:
Develop a data pipeline to process a large volume of financial transaction data, customer’s social media data and apply rules-based and AI-based algorithms. innovative digital marketing campaigns services can only be possible when banks and financial services providers have the right infrastructure in place, defined by qualities that include:

- cloud-native and agile
- built for streaming and able to handle burst capacity
- integrated with robust security features
- able to provide data insights through AI
- API-enabled

## Recommended Tech Stack:
- Cloud: AWS
- Data Storage: AWS S3/ Redshift
- Data Engineering ETL/ELT: Spark(PySpark) / Databricks / Glue
- Real Time data ingestion: Amazon Managed Streaming for Apache Kafka (Amazon MSK)
- Orchestration: Amazon Managed Workflows for Apache Airflow (MWAA)

## Judging Criteria:
- Usefulness and Completeness 25%
- Methodological soundness or Innovative approach 25%
- Replicability and Performance on (volume, variety, velocity, and veracity of data) 20%
- Novelty or Originality 15%
- Quality of presentation, and quantitative analysis when applicable being preferred 15%

## Deliverables:
- A powerpoint presentation which should contain a description of what you have tried to build. (Download Sample PPT)
1. what problem you are solve
2. solution approach
3. Any supporting assumptions, functional requirements(FR) and non-functional requirements(NFR)
4. list of AWS services used with reasoning
5. reason why your solution should be considered for the final round
6. Source code (Submit your Code in Python only)
- Demonstration Video showing the functionalities/working of the solution.


## OS/Python Environment Setup

```bash
sudo apt-get update
sudo apt-get install zip sed wget -y
```

## Building Lambda Package

```bash
cd deployment 
chmod +x ./build-s3-dist.sh
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