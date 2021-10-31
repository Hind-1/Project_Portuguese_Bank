# Project Portuguese Bank


## Backstory:
  The Portuguese Bank's customers haven't investigated enough for long term deposits, which that leads to revenue decline. To fix the issue, the bank will be identified the customers who have chance to subscribe for long-term deposit. Then, the marketing campaign will be focused on those customers. 

## Data Set Information:
  The data is related to direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, to access if the product (bank term deposit) would be subscribed ('yes') or not ('no') subscribed.
There are two datasets: test.csv with all observations (32950) and 16 inputs including the target feature. 


## Goal: 
 The classification goal is to predict if the client will subscribe (yes/no) a term deposit (variable y).



## The dataset:
   We obtained the dataset from Kaggle website (Banking Dataset) which targets people who people have chance to subscribe for long-term deposit (yes-no), (structured dataset), containing 16 features and 32,950 observations with extension csv. The data contains the following columns:




## Feature Description
- age  
age of a person
- job  
type of job ('admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')
- marital  
marital status ('divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)
- education  
('basic.4y','basic.6y','basic.9y','high. school','illiterate','professional.course','university.degree','unknown')
- default  
has credit in default? ('no','yes','unknown')
- housing  
has housing loan? ('no','yes','unknown')
- loan 
has personal loan? ('no','yes','unknown')
- contact  
contact communication type ('cellular','telephone')
- month  
last contact month of year ('jan', 'feb', 'mar', …, 'nov', 'dec')
- dayofweek  
last contact day of the week ('mon','tue','wed','thu','fri')
- duration  
last contact duration, in seconds . Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no')
- campaign  
number of contacts performed during this campaign and for this client (includes last contact)
- pdays  
number of days that passed by after the client was last contacted from a previous campaign (999 means client was not previously contacted)
- previous  
number of contacts performed before this campaign and for this client
- poutcome  
outcome of the previous marketing campaign ('failure','nonexistent','success')

Target variable (desired output):
Feature  Feature_Type  Description
y  binary  has the client subscribed a term deposit? ('yes','no')

## Citation:
   Banking Dataset Classification | Kaggle:
   https://www.kaggle.com/rashmiranu/banking-dataset-classification?select=new_test.csv    
   Additional dataset:
   https://www.kaggle.com/berkayalan/bank-marketing-data-set

## Tools:
-   The used tool is SQL.
-   Python Libraries: Numpy, matplotlib, seaborn, sklearn ,pandas and 
-   In addition, creating and evaluating classification  Model.
