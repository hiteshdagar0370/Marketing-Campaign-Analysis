SELECT COUNT(*) AS Total_Customers
FROM marketi*g_customers;

SELECT
AVG(Income) AS Avg_Income
FROM marketing_customers;

SELECT
Response,
COUNT(*) AS Customers
FROM marketing_customers
GROUP BY Response;

SELECT
Education,
AVG(Total_Spend) AS Avg_Spend
FROM marketing_customers
GROUP BY Education
ORDER BY Avg_Spend DESC;

SELECT
Marital_Status,
AVG(Total_Spend) AS Avg_Spend
FROM marketing_customers
GROUP BY Marital_Status;
