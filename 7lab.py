import matplotlib.pyplot as plt

# ----------- Line Plot: Monthly Sales -----------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20000, 25000, 22000, 27000, 30000, 28000]

plt.figure(figsize=(6,4))
plt.plot(months, sales, marker='o', color='blue', linestyle='-')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales (₹)")
plt.grid(True)
plt.show()


# ----------- Pie Chart: Expense Distribution -----------
categories = ["Rent", "Salary", "Utilities", "Marketing", "Misc"]
expenses = [30000, 50000, 10000, 15000, 5000]

plt.figure(figsize=(6,6))
plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title("Expense Distribution")
plt.show()