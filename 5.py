import numpy as np

# Original traffic matrix
T = np.array([[120, 80],
              [60, 140]])

# Signal optimization transformation matrix
S = np.array([[1.2, 0],
              [0, 0.9]])

# New traffic distribution
T_new = np.dot(S, T)

print("Original Traffic Matrix:\n", T)
print("\nOptimized Traffic Matrix:\n", T_new)