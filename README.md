# E-Commerce Sales Analysis Project

## Overview
This project analyzes a large e-commerce transactions dataset (536,351 rows) to answer four main business questions about sales trends, product demand, and customer behavior.  
The analysis is done in Python using **Pandas**, **Matplotlib**, and **Seaborn**.

---

## Dataset Summary

**CSV fields:**

- `TransactionNo` – unique ID for each transaction  
- `Date` – date of the transaction  
- `ProductNo` – product code  
- `ProductName` – product description  
- `Price` – unit price of the product  
- `Quantity` – quantity of the product in that line  
- `CustomerNo` – customer identifier  
- `Country` – country of the customer  

In the script, a new column is created:

- `Sales` = `Price * Quantity` (total sales value per line)

Before analysis, rows with missing values and negative quantities (returns/cancellations) are removed.

---

# Business Questions & Findings

## Q1 – Monthly Sales Trend

**Goal:** How do total sales change from month to month?

**What was done:**

- Converted `Date` to a real datetime column.  
- Created a `YearMonth` column from `Date` (e.g., `2019-03`).  
- Grouped by `YearMonth` and summed `Sales`.  
- Plotted a line chart of total sales per month.

**Findings:**

- Sales drop after December and stay lower in early 2019.  
- From May to August, sales slowly increase and stay stable.  
- From September to November, sales rise sharply and reach a peak in November.  
- December shows a sudden drop because the dataset does not contain the full month.

**Insight:** The business has strong **Q4 sales** (likely holiday season) and weaker **Q1** performance.

**Plot:** `plots/monthly_sales_trend.png`

---

## Q2 – Top 10 Most Frequently Purchased Products

**Goal:** Which products are sold the most in terms of quantity?

**What was done:**

- Grouped the data by `ProductName`.  
- Summed the `Quantity` for each product.  
- Sorted in descending order and selected the top 10.  
- Created a horizontal bar chart of total quantity sold.

**Findings:**

- Products like **Popcorn Holder**, **World War 2 Gliders Assorted Designs**, and **Jumbo Bag Red Retrospot** have the highest total quantities.  
- All top products sell roughly between **25,000 and 56,000+ units**.  
- These are mostly small, low-cost, high-turnover items (giftware, décor, party supplies).

**Insight:** A small set of products drives a large share of total unit sales and should be prioritized for stock and promotions.

**Plot:** `plots/top_products.png`

---

## Q3 – Products Purchased per Transaction

**Goal:** How many items do customers typically buy in a single transaction?

**What was done:**

- Grouped by `TransactionNo` and summed `Quantity` per transaction.  
- Built a histogram of total items per transaction.

**Findings:**

- Most transactions contain **between 1 and 100 items**.  
- Medium-sized orders (around 100–300 items) are less common.  
- Large bulk orders (300+ items) exist but are rare, forming a long right tail.

**Insight:** The business is mainly driven by **small retail-style orders**, with occasional **large bulk buyers**.

**Plot:** `plots/products_per_transaction.png`

---

## Q4 – Top 10 Most Profitable Customers

**Goal:** Which customers generate the highest total sales?

**What was done:**

- Grouped the data by `CustomerNo`.  
- Summed `Sales` for each customer.  
- Sorted in descending order and selected the top 10.  
- Created a horizontal bar chart of total sales by customer.

**Findings:**

- Customer **14646** is the standout, generating over **£2M** in total sales.  
- Other top customers contribute roughly **£500k–£1.3M** each.  
- Revenue is clearly concentrated among a small group of customers.

**Insight:** This is a strong **80/20 pattern** – a small number of customers contribute a large share of revenue, so retaining them is critical.

**Plot:** `plots/top_customers.png`

---

# Q5 – Recommendations

Based on the four questions:

1. **Seasonality & campaigns**  
   - Focus marketing and stock planning around **Q4**, when sales spike.  
   - Run campaigns and discounts during weaker months (especially **February–April**) to smooth out the dip.

2. **Inventory management**  
   - Keep top-selling products (from Q2) always in stock.  
   - Monitor their lead times closely and prepare extra stock for peak months.

3. **Increase average order size**  
   - Use bundles and “Frequently Bought Together” suggestions to encourage customers to add more items to each transaction.  
   - Offer discounts when customers buy multiple related products.

4. **High-value customers (Q4)**  
   - Create a simple VIP or loyalty program for top customers (e.g., better prices, early access, priority support).  
   - Monitor their buying patterns to prevent churn and identify upsell opportunities.

5. **Bulk buyers**  
   - Identify customers who regularly place large orders and treat them as a separate segment with wholesale-style offers.

---

# Project Structure

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
