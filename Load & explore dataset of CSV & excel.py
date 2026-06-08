import pandas as pd

# Define the file paths
csv_file_path = 'C:\\Users\\shesh\\CAREER\\SBAB\\BCA 3RD YEAR\\BCA 6TH SEM\\Lab Programs\\ML_Programs\\sample_data.csv'
excel_file_path = 'C:\\Users\\shesh\\CAREER\\SBAB\\BCA 3RD YEAR\\BCA 6TH SEM\\Lab Programs\\ML_Programs\\sample_data.xlsx'

# Load the CSV file
data_csv = pd.read_csv(csv_file_path)
print("CSV File Data:")
print(data_csv)

#load the Excel file
data_excel = pd.read_excel(excel_file_path)
print("\nExcel File Data:")
print(data_excel)

# Basic Data Exploration
print("\nData Descriptions:")
print("CSV Data Description:")
print(data_csv.describe())

print("\nExcel Data Description:")
print(data_excel.describe())

# Displayinf data types
print("\nData Types in CSV File:")
print(data_csv.dtypes)

print("\nData Types in Excel File:")
print(data_excel.dtypes)
