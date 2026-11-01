
import pandas as pd

# Load raw dataset
df = pd.read_csv("logistics_raw_data.csv")

print("========== DATASET OVERVIEW ==========")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 10 Records:")
print(df.head(10))

print("\nColumn Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nShipping Mode Distribution:")
print(df["Shipping_Mode"].value_counts())
