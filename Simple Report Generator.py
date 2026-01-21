# Simple Report Generator

FILE_NAME = "report.txt"

def generate_report():
    name = input("Enter name: ")
    department = input("Enter department: ")
    score = int(input("Enter score (out of 100): "))

    if score >= 80:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 40:
        grade = "C"
    else:
        grade = "Fail"

    with open(FILE_NAME, "a") as file:
        file.write("Name: " + name + "\n")
        file.write("Department: " + department + "\n")
        file.write("Score: " + str(score) + "\n")
        file.write("Grade: " + grade + "\n")
        file.write("---------------------\n")

    print("Report generated successfully!")

def view_reports():
    print("\n--- All Reports ---")
    try:
        with open(FILE_NAME, "r") as file:
            data = file.read()
            if data == "":
                print("No reports found.")
            else:
                print(data)
    except FileNotFoundError:
        print("No report file found.")

choice = 0
while choice != 3:
    print("\n1. Generate Report")
    print("2. View Reports")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        generate_report()
    elif choice == 2:
        view_reports()
    elif choice == 3:
        print("Exiting...")
    else:
        print("Invalid choice")

print("Program finished")