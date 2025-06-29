import pandas as pd
import matplotlib.pyplot as plt
import seaborn

# Reads data from the provided Excel file
df = pd.read_excel("retail_sales_data.xlsx", sheet_name = "Data")

# Makes sure OrderDate is a datetime object and extracts year and month from OrderDate column
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Year'] = df['OrderDate'].dt.year
df['Month'] = df['OrderDate'].dt.to_period("M")

# Groups data by each Region/Category combination, sums the necessary columns, and resets the df to a flat table
pivot = df.groupby(['Region', 'Category']).agg({
    'Quantity': 'sum',
    'UnitPrice': 'sum',
    'TotalSales': 'sum'
    }).reset_index()

# Renames columns to match those in Excel pivot table
pivot = pivot.rename(columns={
    'Quantity': 'Sum of Quantity',
    'UnitPrice': 'Sum of UnitPrice',
    'TotalSales': 'Sum of TotalSales'
})

# Shows the complete pivot table in the console
print("Pivot Table:")
print(pivot)

# Visualisation 1 - Sales by Region
region_sales = df.groupby('Region')['TotalSales'].sum().sort_values()
seaborn.barplot(x=region_sales.values, y=region_sales.index, palette='Blues_r')
plt.title("Total Sales by Region")
plt.xlabel("Total Sales")
plt.savefig("visualisation/total_sales_by_region.png")
plt.show()

# Visualisation 2 - Sales by Region and Category
region_category = df.groupby(['Region', 'Category'])['TotalSales'].sum().reset_index()
seaborn.barplot(data=region_category, x='TotalSales', y='Region', hue='Category')
plt.title("Sales by Region and Category")
plt.savefig("visualisation/sales_by_region_and_category.png")
plt.show()

# Visualisation 3 - Yearly Sales by Category
plt.figure(figsize=(12, 6))
df['Year'] = df['OrderDate'].dt.year
yearly_category_sales = df.groupby(['Year', 'Category'])['TotalSales'].sum().reset_index()
seaborn.barplot(data=yearly_category_sales, x='Year', y='TotalSales', hue='Category', palette='Set2')
plt.title('Total Sales by Year and Category')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("visualisation/yearly_sales_by_category.png")
plt.show()