import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Create total_sales column
df['total_sales'] = df['quantity'] * df['price']

print("First 5 rows:")
print(df.head())

print("\nTotal Revenue:")
print(df['total_sales'].sum())

print("\nTop Selling Product:")
print(df.groupby('product')['quantity'].sum().sort_values(ascending=False))

print("\nSales by City:")
print(df.groupby('city')['total_sales'].sum())

# Bar Chart
df.groupby('product')['total_sales'].sum().plot(kind='bar')
plt.title("Product vs Total Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Pie Chart
df.groupby('category')['total_sales'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title("Category Distribution")
plt.show()

# Line Chart
df['order_date'] = pd.to_datetime(df['order_date'])
df.groupby('order_date')['total_sales'].sum().plot(kind='line')
plt.title("Sales Over Time")
plt.show()