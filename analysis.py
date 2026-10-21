import pandas as pd
df=pd.read_csv("dataset/ecommerce_sales_customer_behavior_500.csv")
print(df.head())

# Display first 5 rows
print("FIRST 5 ROWS:")
print(df.head())

# Display number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# Display column names
print("\nCOLUMN NAMES:")
print(df.columns)

# Display data types
print("\nDATA TYPES:")
print(df.dtypes)

# Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# Convert Order_Date to date format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing discounts with 0
df["Discount_Percent"] = df["Discount_Percent"].fillna(0)

# Make sure numeric columns are numeric
numeric_columns = [
    "Quantity",
    "Unit_Price",
    "Discount_Percent",
    "Sales",
    "Cost",
    "Profit"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Check the cleaned data
print("\nAFTER CLEANING:")
print(df.info())

print("\nMISSING VALUES AFTER CLEANING:")
print(df.isnull().sum())

print("\nDUPLICATES AFTER CLEANING:")
print(df.duplicated().sum())

# ==============================
# STEP 4: SALES ANALYSIS
# ==============================

# Total Sales
total_sales = df["Sales"].sum()
print("\nTOTAL SALES:")
print(round(total_sales, 2))

# Total Profit
total_profit = df["Profit"].sum()
print("\nTOTAL PROFIT:")
print(round(total_profit, 2))

# Total Orders
total_orders = df["Order_ID"].nunique()
print("\nTOTAL ORDERS:")
print(total_orders)

# Total Customers
total_customers = df["Customer_ID"].nunique()
print("\nTOTAL CUSTOMERS:")
print(total_customers)

# Total Quantity Sold
total_quantity = df["Quantity"].sum()
print("\nTOTAL QUANTITY SOLD:")
print(total_quantity)


# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(
    ascending=False
)

print("\nSALES BY CATEGORY:")
print(category_sales)

# Top 10 Products
top_products = df.groupby("Product")["Sales"].sum().sort_values(
    ascending=False
).head(10)

print("\nTOP 10 PRODUCTS:")
print(top_products)

# Sales by Location
location_sales = df.groupby("Location")["Sales"].sum().sort_values(
    ascending=False
)

print("\nSALES BY LOCATION:")
print(location_sales)

# ==============================
# STEP 5: CUSTOMER BEHAVIOUR ANALYSIS
# ==============================

# Total spending by each customer
customer_spending = df.groupby("Customer_ID")["Sales"].sum().sort_values(
    ascending=False
)

print("\nTOP 10 CUSTOMERS BY SPENDING:")
print(customer_spending.head(10))


# Number of orders by each customer
customer_orders = df.groupby("Customer_ID")["Order_ID"].nunique().sort_values(
    ascending=False
)

print("\nTOP 10 CUSTOMERS BY NUMBER OF ORDERS:")
print(customer_orders.head(10))


# Average order value
average_order_value = df["Sales"].mean()

print("\nAVERAGE ORDER VALUE:")
print(round(average_order_value, 2))


# New vs returning customers
orders_per_customer = df.groupby("Customer_ID")["Order_ID"].nunique()

new_customers = (orders_per_customer == 1).sum()
returning_customers = (orders_per_customer > 1).sum()

print("\nNEW CUSTOMERS:")
print(new_customers)

print("\nRETURNING CUSTOMERS:")
print(returning_customers)


# ==============================
# STEP 6: RFM ANALYSIS
# ==============================

# Reference date
reference_date = df["Order_Date"].max() + pd.Timedelta(days=1)

# Calculate RFM values
rfm = df.groupby("Customer_ID").agg({
    "Order_Date": lambda x: (reference_date - x.max()).days,
    "Order_ID": "nunique",
    "Sales": "sum"
})

# Rename columns
rfm.columns = ["Recency", "Frequency", "Monetary"]

print("\nRFM ANALYSIS:")
print(rfm.head(10))

# Create RFM scores
rfm["R_Score"] = pd.qcut(
    rfm["Recency"].rank(method="first"),
    5,
    labels=[5, 4, 3, 2, 1]
).astype(int)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

# Overall RFM score
rfm["RFM_Score"] = (
    rfm["R_Score"] +
    rfm["F_Score"] +
    rfm["M_Score"]
)

print("\nRFM SCORES:")
print(rfm.head(10))

def customer_segment(score):
    if score >= 13:
        return "VIP Customer"
    elif score >= 10:
        return "Loyal Customer"
    elif score >= 7:
        return "Regular Customer"
    else:
        return "Occasional Customer"

rfm["Customer_Segment"] = rfm["RFM_Score"].apply(customer_segment)

print("\nCUSTOMER SEGMENTS:")
print(rfm["Customer_Segment"].value_counts())

# ==============================
# STEP 7: SAVE CLEANED DATA
# ==============================

df.to_csv(
    "dataset/cleaned_ecommerce_sales.csv",
    index=False
)

print("\nCLEANED DATASET SAVED SUCCESSFULLY!")

rfm.to_csv("dataset/customer_rfm_analysis.csv",index=True)
print("\nRFM DATASET SAVED SUCCESSFULLY")