Enabling More Targeted Promotions and Lower Customer Acquisition Costs using Data Engineering and AI

One of Incedo Inc banking and financial services(BFSI) customer wanted to improve their marketing campaigns in order to boost conversion rates while lowering customer acquisition costs. To better target clients and promote the most appropriate products and services, the bank sought to identify channels, offers, and approaches.

The bank decided to collate, aggregate, and analyze a large amount of structured and unstructured data to help identify key indications of interest, including:

Customer purchase and transaction history
Customer profile data
Customer behavior on social media (Twitter, Facebook)
Data Schema:

1. Customer purchase and transaction history
2. Customer profile data

Social Media: Twitter

Twitter Data Dictionary
Twitter Data Entities
Social Media: Facebook
1. Facebook APIs, SDKs & Guides - Facebook Developer Docs


## Problem and Business Objective

- To reduce customer acquisition cost by targeting the ones who are likely to buy
- To improve the response rate, i.e., the fraction of prospects who respond to the campaign

## Data

- ***Customer data:*** Demographic data, data about other financial products like home loans, personal loans, etc.
- ***Campaign data:*** Data about previous campaigns (number of previous calls, number of days since the last call was made, etc.)
- ***Macroeconomic data***
- ***Target variable:*** Response (Yes/No)
    ### bank_marketing.csv data schema
    #### Data Dictionary
    ##### 1. Client Related Data
  - Age ," Age of Prospect,numeric type"
  - Job," Type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')"
  - Marital ," Marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)"
  - Education," Education level (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')"
  - Default," Has credit in default? (categorical: 'no','yes','unknown')"
  - Housing," Has housing loan? (categorical: 'no','yes','unknown')"
  - Loan," Has personal loan? (categorical: 'no','yes','unknown')"
  
  #### 2. Campaign Related Data
  - Contact," Contact communication type (categorical: 'cellular','telephone') "
  - Month," Last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')"
  - Day," Last contact day of the week (categorical: 'mon','tue','wed','thu','fri')"
  - Duration," Last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known   before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model."
  - Campaign," Number of contacts performed during this campaign and for this client (numeric, includes last contact)"
  - Pdays, Number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
  - Previous, Number of contacts performed before this campaign and for this client (numeric)
  - Poutcome," Outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')"
  #### 3. Social and Economic Context Attributes
  - emp.var.rate, Employment variation rate - quarterly indicator (numeric)
  - cons.price.idx, Consumer price index - monthly indicator (numeric) 
  - cons.conf.idx, Consumer confidence index - monthly indicator (numeric) 
  - Euribor3m, Euribor 3 month rate - daily indicator (numeric)
  - nr.employed, Number of employees - quarterly indicator (numeric)

## Tasks

To solve the problem, we should build model without including the variable ‘duration’. Because the prospect data procured by the marketing team does not contain ‘duration’, since the call has not been made yet. This will help us understand the relationship of the other variables with the response.

Also, set the business objective to achieving 80% of total responders at the minimum possible cost. The total number of responders is the total number of prospects who responded, from the available data of about 45,000 prospects.

Based on this information, calculate the X in the top X%, i.e., how many prospects should be called to meet the business objective. 

## Checkpoints

The checkpoints for the assignment are as follows:

1. Perform data preparation and EDA.

2. Build a logistic regression model without using the variable 'duration'

  - Select variables using the usual methods
  - Sort the data points in decreasing order of the probability of response
  - Find the optimal probability cut-off and report the relevant evaluation metrics

3. Create a data frame with the variables prospect ID, actual response, predicted response, predicted probability of response, duration of the call in seconds and cost of the call

4. Find the number of top X% prospects we should target to meet the business objective
  - Report the average call duration for targeting the top X% prospects.

5. Create a lift chart

  - The x-axis should show the number of prospects contacted; the y-axis should show the ratio of the response rate using the model and the response rate without using the model

6. Determine the cost of acquisition for 80% of customers using the predictive model.
