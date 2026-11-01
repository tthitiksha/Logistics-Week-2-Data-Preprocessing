
import pandas as pd
import numpy as np

# Load raw dataset
df = pd.read_csv("logistics_raw_data.csv")

print("BEFORE CLEANING")
print("Rows and columns:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print("Duplicates:", df.duplicated().sum())

# Step 1: Remove duplicate records
df = df.drop_duplicates()

# Step 2: Handle missing numerical values
df["Sales"] = df["Sales"].fillna(df["Sales"].median())

# Step 3: Handle missing categorical values
df["Shipping_Mode"] = df["Shipping_Mode"].fillna(
    df["Shipping_Mode"].mode()[0]
)

# Step 4: Detect and handle unusual delivery values
q1 = df["Shipping_Days_Actual"].quantile(0.25)
q3 = df["Shipping_Days_Actual"].quantile(0.75)

iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outliers = df[
    (df["Shipping_Days_Actual"] < lower_limit) |
    (df["Shipping_Days_Actual"] > upper_limit)
]

print("\nOutliers detected:", len(outliers))

# Cap extreme values using IQR limits
df["Shipping_Days_Actual"] = df[
    "Shipping_Days_Actual"
].clip(lower_limit, upper_limit)

# Save cleaned dataset
df.to_csv("logistics_cleaned_data.csv", index=False)

print("\nAFTER CLEANING")
print("Rows and columns:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print("Duplicates:", df.duplicated().sum())

print("\nCleaned dataset saved successfully!")
