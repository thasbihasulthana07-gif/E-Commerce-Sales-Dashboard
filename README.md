# E-commerce Sales and Customer Behavior Analysis

## 📌 Project Overview
This project analyzes e-commerce sales data and customer purchasing behavior using **Python, Pandas, and Microsoft Power BI**. The goal is to understand sales performance, identify top-selling products, analyze customer spending patterns, and segment customers using RFM analysis.

## 🎯 Objectives
- Analyze total sales, profit, orders, and customers.
- Identify top-performing product categories and products.
- Compare sales across different locations.
- Analyze customer spending and purchasing frequency.
- Identify new and returning customers.
- Segment customers using RFM (Recency, Frequency, Monetary) analysis.
- Create a Power BI dashboard to present key business insights.

## 🛠️ Tools and Technologies
- **Python** – Data analysis and data cleaning
- **Pandas** – Data manipulation and analysis
- **Microsoft Power BI** – Interactive dashboard and visualization
- **CSV** – Dataset storage

## 📂 Project Structure

```text
E-commerce-Sales-Analysis/
│
├── dataset/
│   ├── ecommerce_sales_customer_behavior_500.csv
│   ├── cleaned_ecommerce_sales.csv
│   └── customer_rfm_analysis.csv
│
├── analysis.py
├── E commerce Sales.pbix
└── README.md
```

## 📊 Project Workflow

### 1. Data Cleaning
- Checked missing values and duplicate records.
- Converted order dates into datetime format.
- Filled missing discount values with zero.
- Converted numeric columns into appropriate data types.

### 2. Sales Analysis
- Total sales and total profit
- Total orders and unique customers
- Total quantity sold
- Sales by product category
- Top 10 products by sales
- Sales by location

### 3. Customer Behavior Analysis
- Total spending by customer
- Top 10 customers by spending
- Customers ranked by number of orders
- Average sales value per dataset row
- New versus returning customer analysis

### 4. RFM Analysis
RFM analysis helps understand customer purchasing behavior using three metrics:

- **Recency:** How recently a customer made a purchase.
- **Frequency:** How often a customer places orders.
- **Monetary:** The total amount spent by a customer.

Customers are assigned RFM scores and classified into four segments:
- VIP Customer
- Loyal Customer
- Regular Customer
- Occasional Customer

### 5. Power BI Dashboard
The cleaned sales data is used to build an interactive dashboard for visualizing sales performance and customer behavior.

## 💡 Key Business Benefits
- Understand overall sales and profitability.
- Identify high-performing products and locations.
- Recognize valuable and loyal customers.
- Understand customer purchasing patterns.
- Support data-driven business decisions.

## 🚀 How to Run the Project

1. Download or clone this repository.
2. Install Python on your computer.
3. Install Pandas:

   ```bash
   pip install pandas
   ```

4. Ensure the original CSV dataset is inside the `dataset` folder.
5. Run the Python analysis script:

   ```bash
   python analysis.py
   ```

6. Open `E commerce Sales.pbix` using Microsoft Power BI Desktop to explore the dashboard.

## 📁 Output Files
- `cleaned_ecommerce_sales.csv` – Cleaned sales dataset.
- `customer_rfm_analysis.csv` – Customer RFM scores and segments.
- `E commerce Sales.pbix` – Power BI dashboard.
- analysis.py-data cleaned using python

## 👩‍💻 Author
**Thasbiha Sulthana**

BCA Student | Aspiring Data Analyst

---

*This project demonstrates practical skills in data cleaning, exploratory data analysis, customer segmentation, and business intelligence reporting.*
