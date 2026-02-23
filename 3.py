
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