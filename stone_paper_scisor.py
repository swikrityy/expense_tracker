import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("🎮 Rock Paper Scissors Game 🎮")
print("Type 'exit' to quit\n")

while True:
    user = input("Choose rock, paper, or scissors: ").lower()

    if user == "exit":
        print("\nFinal Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thanks for playing! 👋")
        break

    if user not in choices:
        print("❌ Invalid choice! Try again.\n")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("🤝 It's a tie!\n")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "papar")
    ):
        print("✅ You win this round!\n")
        user_score += 1

    else:
        print("💀 Computer wins this round!\n")
        computer_score += 1