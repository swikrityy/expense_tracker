# Simple Student Information Program

print("Welcome to Student Info System")

# Take inputs
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
math = int(input("Enter marks in Math: "))
science = int(input("Enter marks in Science: "))
english = int(input("Enter marks in English: "))

# Calculate total and percentage
total = math + science + english
percentage = total / 3

# Display results
print("\n----- Student Details -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)

# Result decision
if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("Thank you for using the system")