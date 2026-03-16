import numpy as np

# -------------------------------
# Case 1: Standard Deviation of Weekly Rainfall
# -------------------------------
print("Case 1: Weekly Rainfall Analysis")

# rainfall data in mm for 7 days
rainfall = np.array([12, 15, 20, 18, 10, 25, 17])

std_rainfall = np.std(rainfall)

print("Weekly Rainfall Data:", rainfall)
print("Standard Deviation of Rainfall:", std_rainfall)



