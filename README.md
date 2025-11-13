# E-Commerce Sales Analysis Project

## Overview
This project analyzes a large e-commerce transactions dataset (536,351 rows) to answer four main business questions about sales trends, product demand, and customer behavior.  
The analysis is done in Python using **Pandas**, **Matplotlib**, **Numpy**, and **Seaborn**.

---

## Dataset Summary

### **CSV fields:**
- **TransactionNo** – unique ID for each transaction  
- **Date** – date of the transaction  
- **ProductNo** – product code  
- **ProductName** – product description  
- **Price** – unit price of the product  
- **Quantity** – quantity of the product in that line  
- **CustomerNo** – customer identifier  
- **Country** – country of the customer  

### **New column created:**
- **Sales = Price × Quantity**  
  → total sales value per line.

### **Data cleaning steps:**
- Removed missing values  
- Removed negative quantities (returns/cancellations)  
- Converted `Date` into datetime  
- Created `YearMonth` for monthly analysis  

---

# Business Questions & Findings

---

## Q1 – Monthly Sales Trend

### Goal
Identify how total sales changed month-to-month throughout the dataset.

### What Was Done
- Converted `Date` into a proper datetime format  
- Extracted `YearMonth` for monthly grouping  
- Grouped the dataset by month  
- Calculated total monthly `Sales`  
- Visualized the trend using a line chart  

### Findings
- Sales decline sharply after **December 2018** and remain low through **early 2019**  
- From **May to August**, sales steadily rise and stay relatively stable  
- A major increase appears from **September to November**, with **November being the peak month**  
- **December 2019 shows a sharp drop**, likely because the dataset does **not** include the full month  

### Insight
The business experiences strong **holiday-season demand (Oct–Nov)** and weaker performance in **early-year months**.  
This suggests opportunities for targeted promotions, marketing, and inventory planning during low-sales periods.

**Plot:** `plots/monthly_sales_trend.png`


---

## Q2 – Top 10 Most Frequently Purchased Products

### Goal
Identify which products were sold the most in terms of total quantity.

### What Was Done
- Grouped the dataset by `ProductName`  
- Calculated total `Quantity` sold for each product  
- Sorted the products in descending order  
- Selected the top 10 highest-selling items  
- Created a horizontal bar chart to visualize results  

### Findings
- The top-selling products range from **25,000 to 56,000+ units** sold.  
- The highest-volume items include:  
  - **Popcorn Holder**  
  - **World War 2 Gliders Assorted Designs**  
  - **Jumbo Bag Red Retrospot**  
- Most top products are **small, low-cost, high-turnover gift and novelty items**.  
- These products consistently outperform others in total units sold.

### Insight
A small group of products contributes a large share of total unit sales.  
These items should be prioritized in **inventory planning, restocking, and promotional strategies** to avoid stockouts and maximize revenue.

**Plot:** `plots/top_products.png`


---

## Q3 – Products Purchased per Transaction

### Goal
Understand how many items customers typically buy in a single transaction.

### What Was Done
- Grouped the dataset by `TransactionNo`  
- Calculated total `Quantity` purchased in each transaction  
- Created a histogram to visualize the distribution of items per order  

### Findings
- The majority of transactions contain **between 1 and 100 items**, indicating small to medium retail orders  
- Orders between **100 and 300 items** occur less frequently  
- A small number of transactions exceed **300+ items**, creating a long right-tail  
- Extremely large orders (700–2000 items) are rare but present, suggesting occasional bulk or wholesale buyers  

### Insight
Most customers place **small retail-style orders**, while a minority of buyers place **large bulk purchases**.  
This mix indicates a retail-driven business with occasional wholesale or high-volume clients.

**Plot:** `plots/products_per_transaction.png`


---

## Q4 – Top 10 Most Profitable Customers

### Goal
Identify which customers generated the highest total sales.

### What Was Done
- Calculated line-level `Sales` for each purchase  
- Grouped the dataset by `CustomerNo`  
- Summed total `Sales` per customer  
- Sorted customers in descending order  
- Selected the top 10 highest-revenue customers  
- Visualized results using a horizontal bar chart  

### Findings
- **Customer 14646** stands out significantly, generating **over £2 million** in total sales  
- Other top customers each contribute between **£500,000 and £1.3 million**  
- A small number of customers are responsible for a disproportionately large share of total revenue  
- This indicates heavy reliance on **high-value repeat buyers** or small wholesale clients  

### Insight
The results reflect the classic **80/20 pattern** — a small number of customers contribute the majority of revenue.  
Retaining these high-value customers through loyalty programs, targeted offers, and proactive communication is crucial for sustaining revenue.

**Plot:** `plots/top_customers.png`


---

## Q5 – Recommendations

Based on the sales trends, product performance, customer spending patterns, and transaction behavior observed in the dataset, the following recommendations can help optimize operations and improve revenue:

### 1. Seasonality & Demand Planning
- Increase marketing efforts and inventory levels during **October–November**, when sales peak  
- Introduce promotions, discounts, or targeted campaigns during **February–April**, the slowest months  
- Plan staffing, logistics, and stock replenishment around these seasonal patterns

### 2. Inventory Management
- Prioritize restocking of **top-selling, fast-moving items** (e.g., Popcorn Holder, Gliders, Retrospot bags)  
- Build safety stock ahead of high-demand periods to avoid stockouts  
- Monitor lead times closely for high-turnover products

### 3. Increase Average Basket Size
- Introduce product bundles and curated sets  
- Add “Frequently Bought Together” recommendations  
- Offer tiered or multi-item discounts (e.g., "Buy 3, Get 1 Free")

### 4. Retain High-Value Customers
- Create **VIP or Loyalty Programs** for top-spending customers  
- Offer early access to new items, exclusive discounts, or priority support  
- Track purchasing patterns to identify churn risks early

### 5. Bulk Buyer Strategy
- Identify customers who regularly place **large-volume orders**  
- Provide wholesale-style pricing, custom packaging, or bulk-order incentives  
- Maintain personalized communication to strengthen long-term business relationships


---

## 📁 Project Structure

```text
ecommerce_analysis_project/
│
├── ecommerce_analysis.py
├── sales_transaction.csv
│
├── plots/
│   ├── monthly_sales_trend.png
│   ├── top_products.png
│   ├── products_per_transaction.png
│   └── top_customers.png
│
└── README.md
```

---

## ⚙️ How to Run

Install dependencies:

```bash
pip install pandas matplotlib seaborn numpy
```

Run the script:

```bash
python ecommerce_analysis.py
```

## Glossary of Functions (Pandas + Matplotlib/Seaborn)

### Pandas Functions

| Function | What It Did in This Project |
|---------|------------------------------|
| pd.read_csv() | Loaded the `sales_transaction.csv` dataset into a DataFrame. |
| df.dropna() | Removed missing rows to avoid errors in grouping and calculations. |
| df[df["Quantity"] > 0] | Filtered out negative quantities (returns/cancellations). |
| pd.to_datetime(df["Date"]) | Converted the Date column into proper datetime format. |
| df["YearMonth"] = df["Date"].dt.to_period("M") | Created a month-level field used for monthly sales trends. |
| df["Sales"] = df["Price"] * df["Quantity"] | Calculated total sales value for each line in the dataset. |
| df.groupby("YearMonth")["Sales"].sum() | Computed monthly total sales for Q1 analysis. |
| df.groupby("ProductName")["Quantity"].sum() | Computed total units sold per product for Q2. |
| df.groupby("TransactionNo")["Quantity"].sum() | Found how many items were bought per transaction (Q3). |
| df.groupby("CustomerNo")["Sales"].sum() | Calculated total revenue per customer for Q4. |
| .sort_values(ascending=False) | Sorted results from highest to lowest (used in Q2 & Q4). |
| .head(10) | Selected the top 10 records after sorting. |
| .reset_index() | Converted grouped results back into a clean DataFrame for plotting. |


### Matplotlib & Seaborn Functions

| Function | What It Did in This Project |
|----------|------------------------------|
| plt.figure(figsize=...) | Set figure size for readability. |
| sns.lineplot() | Created the monthly sales trend line chart (Q1). |
| sns.barplot() | Plotted top 10 products and top 10 customers (Q2 & Q4). |
| sns.histplot() | Plotted distribution of items per transaction (Q3). |
| plt.title() | Added chart titles. |
| plt.xlabel(), plt.ylabel() | Set axis labels. |
| plt.xticks(rotation=45) | Rotated labels to prevent overlapping. |
| plt.tight_layout() | Ensured spacing was clean and nothing overlapped. |
| plt.savefig() | Saved all plots into the `plots/` folder. |
