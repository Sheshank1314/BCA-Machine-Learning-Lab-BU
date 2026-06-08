Step 1: Creating CSV and Excel Files with Dummy Data 
• Create CSV File: Open a text editor like Notepad or any other code editor. Enter the following data 
Name, Age, Score
Srikanth, 28,85
Snigdha, 22,78
Mary, 31,92
Save this file as sample_data.csv in the C:\ML_Projects directory.

• Create Excel File: We can use Microsoft Excel or Google Sheets to create this file. Enter the below data: 
Name      Course      Sem
Rajesh     BCA         1
Ramesh     BCA         2
Swati      BCOM        1
Florina    BCOM        3
Pooja      BBA         2
Raghu      BBA         4
Save this file as sample_data.xlsx in the C:\ML_Projects directory. 

Step 2: Python Code to Load and Explore the Data
import pandas as pd

# Define the file paths
csv_file_path = 'C:\\Users\\User\\ML_Programs\\sample_data.csv'
excel_file_path = 'C:\\Users\\User\\ML_Programs\\sample_data.xlsx'

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
