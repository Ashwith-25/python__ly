import pandas as pd

# -----------------------------
# Test Case 1: Load COVID-19 dataset
# -----------------------------
print("Test Case 1: COVID-19 Dataset")

# Load CSV file
covid_data = pd.read_csv("covid_data.csv")

# Display first five records
print("\nFirst Five Records:")
print(covid_data.head())

# Display last five records
print("\nLast Five Records:")
print(covid_data.tail())

# Show dataset information
print("\nDataset Information:")
print(covid_data.info())

# Show statistical summary
print("\nStatistical Summary:")
print(covid_data.describe())
