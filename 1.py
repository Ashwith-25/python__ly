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






# ✅ Scenario 5: Factory Production Analysis
# ❓ Question:

# A factory records production of 3 machines across 3 shifts.
# Shift 2 production is doubled due to overtime work.
# Find the total production per machine and convert the data into a single row format.

# ✅ Answer:
import numpy as np

production = np.array([
    [100, 120, 130],
    [90,  110, 140],
    [80,  100, 120]
])

# Double Shift 2 production (column index 1)
production[:, 1] *= 2

# Total production per machine (row-wise sum)
total = np.sum(production, axis=1)

# Convert to single row
report = production.reshape(1, -1)

print("Updated Production:\n", production)
print("\nTotal Production per Machine:\n", total)
print("\nSingle Row Format:\n", report)