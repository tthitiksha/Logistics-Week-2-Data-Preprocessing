
import pandas as pd
import matplotlib.pyplot as plt
import os

print("Starting visualization...")

raw = pd.read_csv("logistics_raw_data.csv")
cleaned = pd.read_csv("logistics_cleaned_data.csv")

# Find the folder containing this Python file
folder = os.path.dirname(os.path.abspath(__file__))

# Graph 1
missing = raw.isnull().sum()
missing = missing[missing > 0]

plt.figure(figsize=(7, 4))
missing.plot(kind="bar")
plt.title("Missing Values Before Cleaning")
plt.tight_layout()
plt.savefig(os.path.join(folder, "missing_values.png"))
plt.close()

# Graph 2
plt.figure(figsize=(7, 4))
plt.hist(raw["Shipping_Days_Actual"], bins=20,
         alpha=0.6, label="Before Cleaning")
plt.hist(cleaned["Shipping_Days_Actual"], bins=20,
         alpha=0.6, label="After Cleaning")
plt.title("Delivery Days Before and After Cleaning")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(folder, "delivery_comparison.png"))
plt.close()

# Graph 3
plt.figure(figsize=(7, 4))
cleaned["Shipping_Mode"].value_counts().plot(kind="bar")
plt.title("Shipping Mode Distribution")
plt.tight_layout()
plt.savefig(os.path.join(folder, "shipping_modes.png"))
plt.close()

print("\nAll three graphs saved successfully!")
print("Saved location:", folder)
print(os.listdir(folder))
