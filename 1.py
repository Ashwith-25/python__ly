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

# ✅ Scenario 2: Employee Performance Bonus
# ❓ Question:

# A company evaluates 3 employees across 3 tasks.
# As a bonus, Task 3 scores are doubled.
# Convert the updated matrix into a single row format.

# ✅ Answer:
import numpy as np

performance = np.array([
    [70, 80, 75],
    [85, 78, 90],
    [60, 88, 72]
])

# Double Task 3 scores (column index 2)
performance[:, 2] *= 2

# Convert to single row
report = performance.flatten()

print("Updated Performance:\n", performance)
print("\nSingle Row Format:\n", report)

# ✅ Scenario 3: Store Revenue Update
# ❓ Question:

# A company tracks revenue of 3 stores for 3 days.
# Store 1 receives an additional ₹5000 bonus revenue each day.
# Convert the final revenue into a single row format.

# ✅ Answer:
import numpy as np

revenue = np.array([
    [20000, 22000, 25000],
    [18000, 21000, 23000],
    [15000, 17000, 19000]
])

# Add 5000 to Store 1 (row index 0)
revenue[0] += 5000

# Convert to single row
report = revenue.reshape(1, -1)

print("Updated Revenue:\n", revenue)
print("\nSingle Row Report:\n", report)

# ✅ Scenario 4: Website Traffic Promotion
# ❓ Question:

# A company tracks website traffic for 3 pages over 3 weeks.
# As part of a promotion, traffic below 5000 visits is doubled.
# Convert the updated matrix into a single row format.

# ✅ Answer:
import numpy as np

traffic = np.array([
    [4000, 5500, 6000],
    [3000, 4500, 7000],
    [5000, 4800, 5200]
])

# Double traffic below 5000
traffic[traffic < 5000] *= 2

# Convert to single row
report = traffic.flatten()

print("Updated Traffic:\n", traffic)
print("\nSingle Row Format:\n", report)

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