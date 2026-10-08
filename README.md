# Marketing-Campaign-Analysis
Marketing Analytics project using Python, SQL, EDA, Customer Segmentation, and Streamlit Dashboard for campaign performance analysis.
Marketing Campaign Analysis
Project Overview
This project focuses on analyzing customer marketing campaign data to identify valuable customer segments, spending behavior, campaign response patterns, and channel usage preferences.

The objective is to help businesses improve their marketing effectiveness and understand which customer groups are most likely to respond to future campaigns.

Business Problem
A retail company has conducted multiple marketing campaigns and collected customer demographic, spending, and campaign response information.

The company wants to:

Identify high-value customers
Understand campaign performance
Analyze spending behavior
Improve customer targeting
Increase campaign response rates
Dataset Information
The dataset contains customer-level information including:

Demographics
ID
Year_Birth
Education
Marital_Status
Income
Kidhome
Teenhome
Country
Customer Relationship
Dt_Customer
Recency
Product Spending
MntWines
MntFruits
MntMeatProducts
MntFishProducts
MntSweetProducts
MntGoldProds
Purchase Channels
NumDealsPurchases
NumWebPurchases
NumCatalogPurchases
NumStorePurchases
NumWebVisitsMonth
Campaign Information
AcceptedCmp1
AcceptedCmp2
AcceptedCmp3
AcceptedCmp4
AcceptedCmp5
Response
Data Preprocessing
The following preprocessing steps were performed:

Missing value handling
Data type correction
Feature engineering
Customer segmentation
Data cleaning
Derived Features
Age
Age = 2026 - Year_Birth
Children
Children = Kidhome + Teenhome
Total Spend
Total_Spend =
MntWines +
MntFruits +
MntMeatProducts +
MntFishProducts +
MntSweetProducts +
MntGoldProds
Total Purchases
Total_Purchases =
NumWebPurchases +
NumCatalogPurchases +
NumStorePurchases
Exploratory Data Analysis
The analysis includes:

Age Distribution
Income Distribution
Campaign Response Analysis
Education vs Spending
Customer Segmentation
High Spender Analysis
Web Engagement Analysis
Customer Segmentation
Segments Created:

High Income Customers
Income > 75,000

High Spenders
Top 10% customers based on Total Spend

Family Customers
Children > 0

High Web Engagement Customers
NumWebVisitsMonth > 5

Campaign Responders
Response = 1

SQL Analysis
Implemented SQL queries for:

Total Customers
Average Income
Campaign Response Rate
Spending by Education
Spending by Marital Status
SQL file included:

marketing_queries.sql
Dashboard Features
Streamlit Dashboard includes:

Dataset Preview
Total Customer KPI
Average Income KPI
Average Spending KPI
Income Distribution
Spending Distribution
Campaign Response Analysis
Segment Filters
Technologies Used
Python
Pandas
NumPy
SQL
Streamlit
Matplotlib
Seaborn
Project Structure
Marketing-Campaign-Analysis
│
├── Marketing_Campaign_Analysis.ipynb
├── marketing_cleaned.csv
├── marketing_queries.sql
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
How To Run
Install dependencies:

pip install -r requirements.txt
Run Streamlit Dashboard:

streamlit run app.py
Key Business Insights
Higher-income customers generally spend more across product categories.
Customers with high web engagement show stronger campaign interaction.
High spenders contribute significantly to overall revenue.
Education and marital status influence purchasing behavior.
Campaign responders represent valuable target customers for future marketing campaigns.
Recommendations
Focus marketing campaigns on high-income customer segments.
Increase personalized promotions for high spenders.
Improve web-based marketing strategies.
Target customers with previous campaign responses.
Create special loyalty offers for family customers.
Optimize channel-specific campaigns based on customer behavior.

Author
Hitesh Dagar
