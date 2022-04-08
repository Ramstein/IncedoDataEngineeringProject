# IncedoDataEngineeringProject
Enabling More Targeted Promotions and Lower Customer Acquisition Costs using Data Engineering and AI-Incedo

One of Incedo Inc banking and financial services(BFSI) customer wanted to improve their marketing campaigns in order to boost conversion rates while lowering customer acquisition costs. To better target clients and promote the most appropriate products and services, the bank sought to identify channels, offers, and approaches.

The bank decided to collate, aggregate, and analyze a large amount of structured and unstructured data to help identify key indications of interest, including:

Customer purchase and transaction history
Customer profile data
Customer behavior on social media (Twitter, Facebook)
Data Schema:

1. Customer purchase and transaction history
customerNumber (CIF),cardLast4Digits,transactionDate,transactionTime,transactionAmount,transactionType,merchantName,merchantCity,merchantState,merchantZip,stateCode


2. Customer profile data
customerNumber (CIF),dateOfBirth,branchNumber,citizenshipCode,currCountryCode,employmentStatus,incomeInThousands,marketSegment,maritalStatus,stateCode,City,customerOpeningDate,Gender

Social Media: Twitter

Twitter Data Dictionary
Twitter Data Entities
Social Media: Facebook
1. Facebook APIs, SDKs & Guides - Facebook Developer Docs

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
-- a. what problem you are solve
-- b. solution approach
-- c. Any supporting assumptions, functional requirements(FR) and non-functional requirements(NFR)
-- d. list of AWS services used with reasoning
-- e. reason why your solution should be considered for the final round
-- f. Source code (Submit your Code in Python only)
- Demonstration Video showing the functionalities/working of the solution.
