import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Improve plot style
sns.set_style("whitegrid")

# ----------- Student Dataset (Scenario Based) -----------
data = {
    "Student": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Marks": [85, 78, 90, 60, 55, 95, 40, 88],
    "Study_Hours": [5, 4, 6, 3, 2, 7, 1, 5],
    "Attendance": [90, 85, 95, 70, 65, 98, 60, 88],
    "Activities": [2, 3, 1, 4, 5, 2, 3, 2]  # extracurricular activities
}

df = pd.DataFrame(data)

# ----------- Create Subplots -----------
plt.figure(figsize=(12,5))

# 🔹 Boxplot → Detect outliers in Marks
plt.subplot(1, 2, 1)
sns.boxplot(y=df["Marks"])
plt.title("Student Marks Distribution (Outliers Detection)")

# 🔹 Heatmap → Correlation between factors
plt.subplot(1, 2, 2)
corr = df[["Marks", "Study_Hours", "Attendance", "Activities"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Between Student Factors")

# ----------- Display Plots -----------
plt.tight_layout()
plt.show()