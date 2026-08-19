import matplotlib.pyplot as plt

# Data
students = ["Anil", "Rahul", "Suresh", "Ravi", "Kiran"]
marks = [80, 70, 90, 60, 85]

# Bar chart
plt.bar(students, marks)

# Labels and title
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

# Display graph
plt.show()