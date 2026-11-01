
import pandas as pd

df = pd.read_csv("logistics_cleaned_data.csv")

print("DATA VALIDATION REPORT")
print("----------------------")

# Check dataset size
print("Dataset shape:", df.shape)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Check data types
print("\nData types:")
print(df.dtypes)

# Check numeric values
print("\nNumeric summary:")
print(df.describe())

# Final validation
if df.isnull().sum().sum() == 0 and df.duplicated().sum() == 0:
    print("\nSUCCESS: Dataset is clean!")
else:
    print("\nWARNING: Some issues remain.")
