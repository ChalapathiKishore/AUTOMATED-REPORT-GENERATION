import pandas as pd
from fpdf import FPDF

# Step 1: Read data from CSV
df = pd.read_csv("data.csv")

# Step 2: Perform analysis
summary = df.describe(include='all')
avg_salary = df["Salary"].mean()
max_salary = df["Salary"].max()
min_salary = df["Salary"].min()

# Step 3: Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Employee Salary Report", ln=1, align='C')
pdf.ln(10)

# Basic Summary
pdf.cell(200, 10, txt=f"Total Employees: {len(df)}", ln=1)
pdf.cell(200, 10, txt=f"Average Salary: ${avg_salary:.2f}", ln=1)
pdf.cell(200, 10, txt=f"Highest Salary: ${max_salary}", ln=1)
pdf.cell(200, 10, txt=f"Lowest Salary: ${min_salary}", ln=1)

pdf.ln(10)
pdf.cell(200, 10, txt="Department-wise Breakdown:", ln=1)

# Step 4: Add department summaries
dept_summary = df.groupby("Department")["Salary"].mean().reset_index()
for index, row in dept_summary.iterrows():
    pdf.cell(200, 10, txt=f"{row['Department']}: ${row['Salary']:.2f}", ln=1)

# Step 5: Save the PDF
pdf.output("salary_report_codtech.pdf")

print("✅ Report generated: salary_report_codtech.pdf")
