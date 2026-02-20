from datetime import datetime

def greet_user(name):
    current_time = datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        greeting = "🌅 Good Morning"
    elif 12 <= hour < 17:
        greeting = "☀️ Good Afternoon"
    elif 17 <= hour < 21:
        greeting = "🌆 Good Evening"
    else:
        greeting = "🌙 Good Night"

    print("\n----------------------------")
    print(f"{greeting}, {name}!")
    print("Today is:", current_time.strftime("%A, %d %B %Y"))
    print("Current Time:", current_time.strftime("%I:%M %p"))
    print("----------------------------")

# Main program
name = input("Enter your name: ")
greet_user(name)