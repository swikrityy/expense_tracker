# Attendance Management System

FILE_NAME = "attendance.txt"

def mark_attendance():
    name = input("Enter student name: ")
    status = input("Enter status (Present/Absent): ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{status}\n")

    print("Attendance marked successfully!")

def view_attendance():
    print("\n--- Attendance Records ---")
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
            if not records:
                print("No attendance records found.")
            else:
                for i, record in enumerate(records, start=1):
                    name, status = record.strip().split(",")
                    print(f"{i}. {name} - {status}")
    except FileNotFoundError:
        print("Attendance file not found.")

choice = 0
while choice != 3:
    print("\n1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        mark_attendance()
    elif choice == 2:
        view_attendance()
    elif choice == 3:
        print("Exiting system...")
    else:
        print("Invalid choice")

print("Program finished")