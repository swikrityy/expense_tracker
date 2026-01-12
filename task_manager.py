def add_task(tasks, task):
    tasks.append(task)
    print("Task added.")


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def main():
    tasks = []

    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()