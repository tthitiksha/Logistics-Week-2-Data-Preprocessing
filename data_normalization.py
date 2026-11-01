
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load cleaned dataset
df = pd.read_csv("logistics_cleaned_data.csv")

# Select numerical columns
numeric_columns = [
    "Shipping_Days_Actual",
    "Shipping_Days_Scheduled",
    "Order_Quantity",
    "Sales"
]

# Apply Min-Max Normalization
scaler = MinMaxScaler()

df[numeric_columns] = scaler.fit_transform(
    df[numeric_columns]
)

# Save normalized dataset
df.to_csv("logistics_normalized_data.csv", index=False)

print("NORMALIZATION COMPLETED!")

print("\nFirst five normalized records:")
print(df.head())

print("\nMinimum values:")
print(df[numeric_columns].min())

print("\nMaximum values:")
print(df[numeric_columns].max())

print("\nNormalized dataset saved successfully!")
