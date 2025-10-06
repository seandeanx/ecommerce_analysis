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
plt.show()