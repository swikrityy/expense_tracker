# Simple Login and Register System

FILE_NAME = "users.txt"

def register():
    username = input("Create username: ")
    password = input("Create password: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{username},{password}\n")

    print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    success = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                saved_user, saved_pass = line.strip().split(",")
                if username == saved_user and password == saved_pass:
                    success = True
                    break
    except FileNotFoundError:
        print("No users found. Please register first.")
        return

    if success:
        print("Login successful! Welcome,", username)
    else:
        print("Invalid username or password")

print("Welcome to Login System")

choice = 0
while choice != 3:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 3:
        print("Goodbye!")
    else:
        print("Invalid choice")