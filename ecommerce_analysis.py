#importing libraries for data analysis and vivizualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

print("Packages loaded successfully ")

#QUESTION 1: Monthly Sales Trend

#Loading the dataset
df = pd.read_csv('sales_transaction.csv')
print("Data loaded successfully")

#total sales per row
df["Sales"] = df["Quantity"] * df["Price"]
print(df.head())

df["Date"] = pd.to_datetime(df["Date"], errors='coerce') #fix date format
print(df["Date"].head()) #checking if date is fixed

df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)  # extract year-month
print("YearMonth column created ") #checking if YearMonth is created

print(df[["Date", "YearMonth"]].head())     # check new column


# group by month & sum sales
df = df.dropna(subset=["Date","Sales"])
df["YearMonth_Period"] = df["Date"].dt.to_period("M")
monthly_sales = (
    df.groupby("YearMonth_Period", as_index=False)["Sales"]
      .sum()
      .sort_values("YearMonth_Period")
)
monthly_sales["YearMonth"] = monthly_sales["YearMonth_Period"].astype(str)
print("Monthly totals:")
print(monthly_sales.head(10).to_string(index=False))

#visualize monthly sales trend
plt.figure(figsize=(10,5))
sns.lineplot(data=monthly_sales, x="YearMonth", y="Sales", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales (£)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/monthly_sales_trend.png")
plt.show()


#QUESTION 2: Most Frequently Purchased Products
# group products and sum quantities

#QUESTION 2: Most Frequently Purchased Products

# group products and sum total quantity sold
product_counts = df.groupby("ProductName")["Quantity"].sum()

# sort products by quantity (highest first)
product_counts = product_counts.sort_values(ascending=False)

# show top 10 most purchased products
print("Top 10 most purchased products (by quantity):")
print(product_counts.head(10))

# turn into DataFrame for plotting
top10_products = product_counts.head(10).reset_index()  # gives columns: Product, Quantity

# visualize top 10 products
plt.figure(figsize=(10, 5))
sns.barplot(data=top10_products, x="Quantity", y="ProductName")
plt.title("Top 10 Most Frequently Purchased Products")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("plots/top_products.png")
plt.show()


#QUESTION 3: Products per Transaction

# remove cancelled transactions (negative quantities)
df_clean = df[df["Quantity"] > 0]

# group by transaction number and sum quantity purchased
transaction_counts = df_clean.groupby("TransactionNo")["Quantity"].sum()

# convert to DataFrame
transaction_counts_df = transaction_counts.reset_index()
transaction_counts_df.columns = ["TransactionNo", "TotalProducts"]

# remove extreme outliers (bulk wholesale orders)
transaction_counts_df = transaction_counts_df[transaction_counts_df["TotalProducts"] < 2000]

# preview
print("Products purchased per transaction (after cleaning):")
print(transaction_counts_df.head(10))

#plot clean histogram
plt.figure(figsize=(10, 5))
sns.histplot(transaction_counts_df["TotalProducts"], bins=30, kde=False)
plt.title("Distribution of Products Purchased per Transaction")
plt.xlabel("Number of Products Purchased")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.savefig("plots/products_per_transaction.png")
plt.show()

#QUESTION 4: Most Profitable Customers

# remove cancelled transactions (negative quantities)
df_clean = df[df["Quantity"] > 0]

# calculate total sales per customer
customer_sales = df_clean.groupby("CustomerNo")["Sales"].sum()

# sort customers by total sales (highest first)
customer_sales = customer_sales.sort_values(ascending=False)

# show top 10 profitable customers
print("Top 10 most profitable customers:")
print(customer_sales.head(10))

# convert to DataFrame for plotting
top10_customers = customer_sales.head(10).reset_index()
top10_customers.columns = ["CustomerNo", "TotalSales"]

# visualize top 10
plt.figure(figsize=(10, 5))
sns.barplot(data=top10_customers, x="TotalSales", y="CustomerNo")
plt.title("Top 10 Most Profitable Customers")
plt.xlabel("Total Sales (£)")
plt.ylabel("Customer ID")
plt.tight_layout()
plt.savefig("plots/top_customers.png")
plt.show()
