# Logistics Data Preprocessing – Week 2

## 1. Project Overview

This project focuses on preprocessing logistics data using Python. It demonstrates the steps involved in inspecting, cleaning, normalizing, visualizing, and validating a dataset to make it suitable for further analysis.

The project uses a simulated logistics dataset generated using Python.

## 2. Objectives

- Inspect the raw logistics dataset.
- Identify and handle missing values.
- Detect and remove duplicate records.
- Identify and treat outliers.
- Normalize numerical features.
- Visualize important data patterns.
- Validate the final cleaned dataset.

## 3. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Visual Studio Code
- GitHub

## 4. Dataset Description

A simulated logistics dataset was generated using Python.

The initial dataset contains 503 rows and 8 columns.

### Features

- Order_ID
- Shipping_Mode
- Order_Region
- Shipping_Days_Actual
- Shipping_Days_Scheduled
- Order_Quantity
- Sales
- Delivery_Status

## 5. Data Preprocessing Steps

### Data Inspection
Inspected the dataset to identify missing values, duplicate records, data types, and statistical summaries.

### Missing Value Treatment
- Filled missing Sales values using the median.
- Filled missing Shipping_Mode values using the mode.

### Duplicate Removal
Removed duplicate records from the dataset.

### Outlier Treatment
Used the Interquartile Range (IQR) method to identify and cap outliers in Shipping_Days_Actual.

### Data Normalization
Applied Min-Max normalization to selected numerical columns using Scikit-learn.

## 6. Data Visualization

The following visualizations were generated:

1. Missing Values
2. Delivery Comparison
3. Shipping Modes

## 7. Validation Results

The final cleaned dataset contains:

| Metric | Result |
|---|---:|
| Rows | 500 |
| Columns | 8 |
| Missing Values | 0 |
| Duplicate Rows | 0 |

The validation script confirmed that the cleaned dataset contains no missing values or duplicate rows.

## 8. Project Files

- `generate_dataset.py` – Generates the simulated dataset.
- `data_inspection.py` – Inspects the raw dataset.
- `data_cleaning.py` – Cleans missing values, duplicates, and outliers.
- `data_normalization.py` – Performs Min-Max normalization.
- `data_visualization.py` – Generates visualizations.
- `data_validation.py` – Validates the cleaned dataset.
- `logistics_raw_data.csv` – Original dataset.
- `logistics_cleaned_data.csv` – Cleaned dataset.
- `logistics_normalized_data.csv` – Normalized dataset.

## 9. How to Run the Project

Install the required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

Run the scripts in this order:

```bash
python generate_dataset.py
python data_inspection.py
python data_cleaning.py
python data_normalization.py
python data_visualization.py
python data_validation.py
```

## 10. Conclusion

This project provided practical experience in data preprocessing using Python. It demonstrated how to improve data quality through missing-value treatment, duplicate removal, outlier handling, normalization, visualization, and validation.

The final cleaned dataset is ready for further logistics data analysis.

---

**Project:** Logistics Data Preprocessing – Week 2  
**Author:** T Thitiksha Ritu