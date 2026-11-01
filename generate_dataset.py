
import pandas as pd
import numpy as np

# Make results reproducible
np.random.seed(42)

# Generate 500 logistics shipment records
n = 500

data = {
    "Order_ID": range(1001, 1001 + n),
    "Shipping_Mode": np.random.choice(
        ["Standard Class", "Second Class", "First Class", "Same Day"], n
    ),
    "Order_Region": np.random.choice(
        ["East", "West", "North", "South"], n
    ),
    "Shipping_Days_Actual": np.random.randint(1, 15, n),
    "Shipping_Days_Scheduled": np.random.randint(2, 10, n),
    "Order_Quantity": np.random.randint(1, 11, n),
    "Sales": np.random.randint(100, 10000, n),
    "Delivery_Status": np.random.choice(
        ["On Time", "Late", "Early"], n
    )
}

df = pd.DataFrame(data)

# Introduce missing values
df.loc[10:19, "Sales"] = np.nan
df.loc[30:34, "Shipping_Mode"] = np.nan

# Introduce duplicate records
df = pd.concat([df, df.iloc[[5, 10, 15]]], ignore_index=True)

# Introduce unusual delivery-time values
df.loc[40, "Shipping_Days_Actual"] = 100
df.loc[41, "Shipping_Days_Actual"] = 120

# Save dataset
df.to_csv("logistics_raw_data.csv", index=False)

print("Dataset generated successfully!")
print("Dataset shape:", df.shape)
print("\nFirst five records:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate records:", df.duplicated().sum())
