-- Display all records
SELECT * FROM sales_data;

-- Total revenue
SELECT SUM(quantity * price) AS total_revenue FROM sales_data;

-- Top selling product
SELECT product, SUM(quantity) AS total_qty
FROM sales_data
GROUP BY product
ORDER BY total_qty DESC;

-- Revenue by city
SELECT city, SUM(quantity * price) AS revenue
FROM sales_data
GROUP BY city;

-- Category-wise revenue
SELECT category, SUM(quantity * price) AS revenue
FROM sales_data
GROUP BY category;

-- Highest value order
SELECT *, (quantity * price) AS total
FROM sales_data
ORDER BY total DESC
LIMIT 1;

-- Average price
SELECT AVG(price) FROM sales_data;