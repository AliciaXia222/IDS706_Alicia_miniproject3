[![CI](https://github.com/AliciaXia222/IDS_706_miniproject_1/actions/workflows/cicd.yml/badge.svg)](https://github.com/AliciaXia222/IDS_706_miniproject_1/actions/workflows/cicd.yml)

# IDS_706_miniproject_3-Country Population Growth
## Prepare develope environment
    * Log in to github 
    * Going into project1 to use template
    * luanch Codespace
    * wait for setting up environment
    * Test on Makefile to use make format, make lint, make test to make sure code format follow the rule.

<img width="1405" alt="Screenshot 2023-09-17 at 5 05 55 PM" src="https://github.com/nogibjj/IDS706_Alicia_miniproject3/assets/143651934/b94659af-4b49-40a8-88a2-40178ae03f27">
<img width="1405" alt="Screenshot 2023-09-17 at 5 05 35 PM" src="https://github.com/nogibjj/IDS706_Alicia_miniproject3/assets/143651934/ac5b1325-be8e-479a-9cc7-3f453352f414">

## Purpose

* This repo is to translate the project 2's code with Pandas package into Polars
* Apply basic EDA on a Country Population Growth Data 
* Plot the Histogram of Growth% in year 2022

## Descriptive statistics:

* The data has 67 columns and 266 entries.
    * 4 rows of categorical data
    * 63 columns of numerical data
    * no data points under 1960 year variable
    * except 1960 column, there are non-null in other columns
* This time only pulled recent 4 years to do the summary, the picture as follow

<img width="524" alt="Screenshot 2023-09-17 at 5 07 26 PM" src="https://github.com/nogibjj/IDS706_Alicia_miniproject3/assets/143651934/a5392b17-84bb-4caf-abb5-0e31f8f4908a">

## Data Viz:

* Below is histogram of 2022 years world population growth plot, the data points mostly concentrate around 1.25% which means the population in each country more likely increased in 2022.

<img width="737" alt="Screenshot 2023-09-17 at 5 07 16 PM" src="https://github.com/nogibjj/IDS706_Alicia_miniproject3/assets/143651934/fc7efa25-7750-41be-9c63-36e8f3ce2a0f">

## Python Script:

<img width="626" alt="Screenshot 2023-09-17 at 5 22 11 PM" src="https://github.com/nogibjj/IDS706_Alicia_miniproject3/assets/143651934/d8c7565e-cc13-4655-b929-fb9a55192443">

## Generated summary report:

* Please see "project3 report.pdf"