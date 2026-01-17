# Contact Book using File Handling

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    with open("contacts.txt", "a") as file:
        file.write(name + " - " + phone + "\n")

    print("Contact saved successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    try:
        with open("contacts.txt", "r") as file:
            data = file.read()
            if data == "":
                print("No contacts found.")
            else:
                print(data)
    except FileNotFoundError:
        print("No contacts file found.")

print("Welcome to Contact Book")

choice = 0
while choice != 3:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        print("Goodbye!")
    else:
        print("Invalid choice")