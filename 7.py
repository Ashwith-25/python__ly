import numpy as np
# -------------------------------
# Case 3: Meteorologist Temperature Analysis
# -------------------------------
print("\nCase 3: Daily Temperature Analysis")

# daily temperature data in degree Celsius
temperature = np.array([30, 32, 31, 29, 35, 36, 33, 34])

mean_temp = np.mean(temperature)
variance_temp = np.var(temperature)
std_temp = np.std(temperature)

print("Daily Temperature Data:", temperature)
print("Mean Temperature:", mean_temp)
print("Variance:", variance_temp)
print("Standard Deviation:", std_temp)