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

