import numpy as np

# Step 1: Original Traffic Matrix
# Rows: [East-West, North-South]
# Columns: [Straight, Turn]

T = np.array([[120, 80],     # East-West traffic
              [60, 140]])    # North-South traffic

# Step 2: Signal Optimization Transformation Matrix
# 1.2 -> Increase East-West by 20%
# 0.9 -> Decrease North-South by 10%

S = np.array([[1.2, 0],
              [0, 0.9]])

# Step 3: Apply transformation
T_new = np.dot(S, T)

# Step 4: Print results
print("Original Traffic Matrix:\n", T)
print("\nOptimized Traffic Matrix:\n", T_new)