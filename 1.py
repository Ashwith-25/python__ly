# ✅ Scenario 1: Monthly Sales Report
# ❓ Question:

# A company records sales of 3 products for 3 months in a 3×3 matrix.
# During a festival, Month 2 sales are doubled.
# Convert the final sales data into a single row format for reporting.

# ✅ Answer:
import numpy as np

# Rows -> Products, Columns -> Months
sales = np.array([
    [10000, 12000, 15000],
    [8000,  9000,  11000],
    [9500,  10500, 13000]
])

# Double Month 2 sales (column index 1)
sales[:, 1] *= 2

# Convert to single row
report = sales.reshape(1, -1)

print("Updated Sales:\n", sales)
print("\nSingle Row Report:\n", report)
