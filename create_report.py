from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document()

# Title
title = doc.add_heading(
    "WEEK 2: LOGISTICS DATA PREPROCESSING", 0
)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

p = doc.add_paragraph(
    "Data Cleaning, Normalization, Visualization and Validation"
)
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph("Project Report")
doc.add_paragraph("Dataset: Simulated Logistics Dataset (500 records)")
doc.add_paragraph("Tools: Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn")

def section(heading, content):
    doc.add_heading(heading, level=1)
    doc.add_paragraph(content)

section(
    "1. Introduction",
    "This project focuses on preparing logistics data for analysis. "
    "The workflow includes data generation, inspection, cleaning, "
    "normalization, visualization and validation."
)

section(
    "2. Dataset Description",
    "A simulated logistics dataset was generated using Python with "
    "503 initial rows and 8 columns. It contains order IDs, shipping "
    "modes, regions, actual and scheduled shipping days, order "
    "quantity, sales and delivery status. The dataset was created "
    "for practice and is not a downloaded public dataset."
)

section(
    "3. Data Inspection",
    "The raw dataset was inspected using Pandas. Missing values, "
    "duplicate records, data types and numeric summaries were checked. "
    "The initial dataset contained 10 missing Sales values, 5 missing "
    "Shipping_Mode values and 3 duplicate rows."
)

section(
    "4. Data Cleaning",
    "Duplicate rows were removed. Missing Sales values were filled "
    "using the median, while missing Shipping_Mode values were filled "
    "using the mode. Outliers in Shipping_Days_Actual were identified "
    "using the Interquartile Range (IQR) method and capped."
)

section(
    "5. Data Normalization",
    "Min-Max normalization was applied to Shipping_Days_Actual, "
    "Shipping_Days_Scheduled, Order_Quantity and Sales using "
    "Scikit-learn's MinMaxScaler. This scales the selected values "
    "to a range between 0 and 1."
)

doc.add_paragraph(
    "Formula: X_scaled = (X - X_min) / (X_max - X_min)"
)

section(
    "6. Data Visualization",
    "Three visualizations were created to examine missing values, "
    "delivery comparisons and shipping modes."
)

for filename, heading in [
    ("missing_values.png", "Missing Values"),
    ("delivery_comparison.png", "Delivery Comparison"),
    ("shipping_modes.png", "Shipping Modes")
]:
    doc.add_heading(heading, level=2)
    if os.path.exists(filename):
        doc.add_picture(filename, width=Inches(5.5))
    else:
        doc.add_paragraph(
            f"Graph not found: {filename}. Insert it manually."
        )

section(
    "7. Data Validation",
    "The final cleaned dataset contains 500 rows and 8 columns. "
    "Validation confirmed zero missing values and zero duplicate rows. "
    "The minimum Shipping_Days_Actual value was 1 and the maximum "
    "was 21.5 after outlier treatment. The validation script reported "
    "that the dataset was clean."
)

section(
    "8. Conclusion",
    "The project successfully demonstrated a complete logistics "
    "data preprocessing workflow. The cleaned dataset is more "
    "consistent and ready for further analysis. The project also "
    "provided practical experience with Python data-processing and "
    "visualization libraries."
)

doc.add_heading("9. Project Files", level=1)
doc.add_paragraph(
    "Python scripts: dataset generation, inspection, cleaning, "
    "normalization, visualization and validation."
)
doc.add_paragraph(
    "CSV files: raw, cleaned and normalized logistics datasets."
)
doc.add_paragraph(
    "PNG files: missing values, delivery comparison and shipping modes."
)

doc.save("Week_2_Logistics_Data_Preprocessing_Report.docx")

print("Report created successfully!")