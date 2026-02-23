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