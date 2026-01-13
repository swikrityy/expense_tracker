# Simple Banking System

balance = 0  # Initial balance

def show_balance():
    print("Your current balance is: $", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Deposited $", amount)
    show_balance()

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print("Withdrew $", amount)
        show_balance()

# Main program
print("Welcome to Simple Bank!")

while True:
    print("\nPlease choose an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)
    elif choice == '4':
        print("Thank you for banking with us! Goodbye.")
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")# Simple Banking System

balance = 0  # Initial balance

def show_balance():
    print("Your current balance is: $", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Deposited $", amount)
    show_balance()

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print("Withdrew $", amount)
        show_balance()

# Main program
print("Welcome to Simple Bank!")

while True:
    print("\nPlease choose an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)
    elif choice == '4':
        print("Thank you for banking with us! Goodbye.")
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")