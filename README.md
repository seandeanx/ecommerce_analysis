# E-Commerce Sales Analysis Project

## Overview
This project analyzes a large e-commerce transactions dataset (536,351 rows) to answer four main business questions about sales trends, product demand, and customer behavior.  
The analysis is done in Python using **Pandas**, **Matplotlib**, and **Seaborn**.

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

### **Goal**
Identify monthly changes in total sales.

### **What Was Done**
- Converted `Date` to datetime  
- Extracted `YearMonth`  
- Grouped by month  
- Summed `Sales`  
- Created a monthly line chart  

### **Findings**
- Sales drop after December  
- Stable growth from May → August  
- Sharp spike from September → November  
- December drops due to incomplete data  

### **Insight**
Strong **Q4 seasonal demand** → likely holiday-driven.  
Weak **Q1** → opportunity for targeted promotions.

**Plot:** `plots/monthly_sales_trend.png`

---

## Q2 – Top 10 Most Frequently Purchased Products

### **Goal**
Identify which products sell the highest quantities.

### **What Was Done**
- Grouped by `ProductName`  
- Summed total `Quantity`  
- Sorted descending  
- Selected top 10  
- Plotted horizontal bar chart  

### **Findings**
- Top sellers (25,000–56,000+ units):  
  - Popcorn Holder  
  - WW2 Gliders Assorted Designs  
  - Jumbo Bag Red Retrospot  
- Mostly giftware & small fast-moving items  

### **Insight**
A small set of products drives the majority of unit sales → keep these fully stocked.

**Plot:** `plots/top_products.png`

---

## Q3 – Products Purchased per Transaction

### **Goal**
Understand how many items customers buy in each order.

### **What Was Done**
- Grouped by `TransactionNo`  
- Summed `Quantity` per transaction  
- Built a histogram  

### **Findings**
- Most transactions have **1–100 items**  
- Medium (100–300) orders less common  
- Rare bulk orders (300+) create a long right-tail  

### **Insight**
Business is mostly **small retail orders**, with occasional bulk purchases.

**Plot:** `plots/products_per_transaction.png`

---

## Q4 – Top 10 Most Profitable Customers

### **Goal**
Find the customers who generate the highest sales.

### **What Was Done**
- Calculated line-level sales  
- Grouped by `CustomerNo`  
- Summed total `Sales`  
- Sorted descending  
- Selected top 10  

### **Findings**
- Customer **14646** generated **£2M+**  
- Others generate **£500K–£1.3M**  
- Revenue is highly concentrated  

### **Insight**
Clear **80/20 rule** — small group of customers → majority of revenue.  
High-value customers must be retained.

**Plot:** `plots/top_customers.png`

---

# Q5 – Recommendations

### **Seasonality**
- Focus marketing + inventory on **Q4**  
- Boost **Feb–Apr** with discounts  

### **Inventory Management**
- Always stock top products  
- Prepare extra inventory ahead of peak months  

### **Increase Basket Size**
- Bundle deals  
- “Frequently Bought Together”  
- Multi-item discounts  

### **Retention of High-Value Customers**
- VIP / loyalty programs  
- Personalized offers  
- Analyze order cycles to prevent churn  

### **Bulk Buyers Strategy**
- Identify large-order customers  
- Offer wholesale pricing or special packages  

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

---
## ⚙️ How to Run

Install dependencies:

```bash
pip install pandas matplotlib seaborn numpy

Then run the script

python ecommerce_analysis.py



