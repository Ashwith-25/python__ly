import pandas as pd
data = {
    'region': ['North','South','East','West','North','South','East','West'],
    'product': ['A','A','B','B','B','C','A','C'],
    'sales': [1000,1500,2000,1200,1800,1700,1600,1400]
}

df = pd.DataFrame(data)

# Region-wise analysis
region_perf = df.groupby('region')['sales'].sum()

# Product-wise analysis
product_perf = df.groupby('product')['sales'].sum()

# Region + Product
combined = df.groupby(['region','product'])['sales'].sum()

print("Region Performance:\n", region_perf)
print("\nProduct Performance:\n", product_perf)
print("\nRegion-Product Performance:\n", combined)