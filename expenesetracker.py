# Simple Expense Tracker

FILE_NAME = "expenses.txt"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, etc): ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount}\n")

    print("Expense added successfully!")

def view_expenses():
    print("\n--- Expense List ---")
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                date, category, amount = line.strip().split(",")
                print(f"{date} | {category} | Rs {amount}")
                total += float(amount)

        print("\nTotal Expense: Rs", total)
    except FileNotFoundError:
        print("No expenses found.")

choice = 0
while choice != 3:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        print("Goodbye!")
    else:
        print("Invalid choice")

print("Program ended")