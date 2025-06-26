# AUTOMATED-REPORT-GENERATION
COMPANY: CODTECH IT SOLUTIONS
NAME:  C Kishore
INTERN ID: CT06DN863
DOMAIN: Python Programming
DURATION: 6 weeks
MENTOR: NEELA SANTOSH

📄 Internship Task 2 – Automated Report Generation
Objective:
The main objective of this task was to develop a Python script that reads structured data from a file, performs basic data analysis, and generates a professionally formatted PDF report using a library such as FPDF or ReportLab. This is a crucial real-world automation skill used in various industries for reporting and documentation.

Project Overview:
For this task, I chose to create a script that analyzes employee salary data stored in a CSV file named data.csv. The script reads the file, processes the data using the pandas library, computes useful insights such as average salary, highest and lowest salary, and department-wise average salaries. Then, it generates a well-structured PDF report using the FPDF library.

Step-by-Step Implementation:
1. Data Preparation:
The dataset (data.csv) was created manually for demonstration. It contains columns such as Name, Department, and Salary. The dataset was designed to be simple yet realistic, with data for five employees across different departments like Engineering, HR, and Marketing.

2. Reading the Data:
Using pandas, the script reads the CSV file into a DataFrame. This allows for easy data manipulation and summarization. Once the data is loaded, basic checks like displaying the head of the DataFrame and verifying column names were performed to ensure accuracy.

3. Data Analysis:
Basic analysis included:

Total number of employees.

Average salary of all employees.

Highest and lowest salaries.

Average salary per department using groupby.

These statistics were computed using simple pandas operations like .mean(), .max(), .min(), and .groupby().

4. Report Generation with FPDF:
FPDF is a lightweight library that allows creation of PDF documents using Python. I initialized a new PDF document, set the font, added a title, and wrote each line of statistical output as individual text cells.

For better readability, section headers like "Department-wise Breakdown" were added, followed by listing each department with its average salary. Adequate spacing and alignment were maintained to give the document a clean, formal look.

5. Saving the Report:
Finally, the PDF was saved with the filename salary_report_codtech.pdf. The script prints a confirmation message once the report is generated.

Files Included in Submission:
report_generator.py – the Python script performing the full task.

data.csv – the input data file used by the script.

salary_report_codtech.pdf – the final PDF report as sample output.

These files were uploaded together in a GitHub repository to maintain project structure and reproducibility.

Conclusion:
This project showcases a practical automation use-case: reading data, analyzing it, and exporting the results into a readable, portable document. It demonstrates proficiency in data handling with pandas and PDF generation using FPDF. This type of task is common in business reporting, HR systems, and data monitoring dashboards. Completing this helped strengthen my skills in Python scripting, data analysis, and report automation, which are highly valued in professional and industrial settings.

![Image](https://github.com/user-attachments/assets/a6da6623-b532-4b13-a036-db2e3162960b)
