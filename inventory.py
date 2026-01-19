# Inventory Management System

FILE_NAME = "inventory.txt"

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{quantity},{price}\n")

    print("Item added successfully!")

def view_items():
    print("\n--- Inventory List ---")
    try:
        with open(FILE_NAME, "r") as file:
            items = file.readlines()
            if not items:
                print("Inventory is empty.")
            else:
                for i, item in enumerate(items, start=1):
                    name, qty, price = item.strip().split(",")
                    print(f"{i}. {name} | Qty: {qty} | Price: Rs {price}")
    except FileNotFoundError:
        print("Inventory file not found.")

def search_item():
    search_name = input("Enter item name to search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, qty, price = line.strip().split(",")
                if name.lower() == search_name.lower():
                    print(f"Found: {name} | Qty: {qty} | Price: Rs {price}")
                    found = True
                    break
        if not found:
            print("Item not found.")
    except FileNotFoundError:
        print("Inventory file not found.")

print("Welcome to Inventory Management System")

choice = 0
while choice != 4:
    print("\n1. Add Item")
    print("2. View Inventory")
    print("3. Search Item")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_item()
    elif choice == 2:
        view_items()
    elif choice == 3:
        search_item()
    elif choice == 4:
        print("Exiting system...")
    else:
        print("Invalid choice")

print("Program ended")