import pandas as pd

#----------------------------- # Test Case 2: Employee Data Analysis # ----------------------------- 
print("\nTest Case 2: Employee Dataset") # Load employee CSV file 
employee_data = pd.read_csv("employee_data.csv") # Display first five records
print("\nFirst Five Records:") 
print(employee_data.head()) # Show dataset structure 
print("\nDataset Information:") 
print(employee_data.info()) # Display statistical summary 
print("\nStatistical Summary:") 
print(employee_data.describe())
