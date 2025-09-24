import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("LIBRARIES IMPORTED SUCESSFULLY")

df = pd.read_csv('sales_transaction.csv')
print("DATA LOADED SUCESSFULLY")

#1How was the sales trend over the months?

df["Sales"] = df["Quantity"] * df["Price"]
print(df.head())

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors='coerce')
print(df["Date"].head())

df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)
print(df["YearMonth"].head())
