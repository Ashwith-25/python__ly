import numpy as np
# -------------------------------
# Case 2: Mean and Median of Student Exam Scores
# -------------------------------
print("\nCase 2: Student Exam Scores Analysis")

scores = np.array([78, 85, 90, 66, 88, 92, 74])

mean_score = np.mean(scores)
median_score = np.median(scores)

print("Student Scores:", scores)
print("Mean Score:", mean_score)
print("Median Score:", median_score)

