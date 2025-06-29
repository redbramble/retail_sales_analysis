# Retail Sales Analysis

This project replicates an Excel Pivot Table analysis using Python. It reads retail sales data from an Excel file and produces summary statistics and visualisations using pandas, matplotlib, and seaborn.

## Files
- `script.py`: Main Python script
- `retail_sales_xlsx`: Excel Spreadsheet containing data to be transformed
- `requirements.txt`: List of Python package dependencies
- `/visualisation/`: Folder where generated charts are saved
- `README.txt`: This file

## Features
- Reads sales data from an Excel file (`retail_sales_data.xlsx`)
- Converts date fields to proper datetime format
- Extracts year and month information for time-based analysis
- Creates a pivot-like summary table (Region x Category)
- Produces the following visualisations:
  - Total Sales by Region (bar chart)
  - Sales by Region and Category (grouped bar chart)
  - Yearly Sales by Category (bar chart)

## How to Run
1. **Set up a virtual environment:**
- python -m venv venv
- source venv/bin/activate

2. **Install dependencies:**
- pip install -r requirements.txt

3. **Run the script:**
- python script.py

This will output a pivot summary table in the terminal and save visualisations to the `visualisation/` folder.