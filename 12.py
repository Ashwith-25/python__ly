import pandas as pd

# Load data
df = pd.read_csv("hr_data.csv")

# Handle missing values
df['PerformanceScore'] = pd.to_numeric(df['PerformanceScore'], errors='coerce')
df['PerformanceScore'].fillna(df['PerformanceScore'].mean(), inplace=True)
df['Department'].fillna("Unknown", inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'], errors='coerce')

# Create performance category
def category(score):
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    else:
        return "Needs Improvement"

df['Category'] = df['PerformanceScore'].apply(category)

# Save cleaned data
df.to_csv("cleaned_hr_data.csv", index=False)

# Show result
print(df.head())