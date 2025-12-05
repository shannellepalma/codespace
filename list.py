def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Edit task")
    print("5. Exit")
    print("===========================")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        # View tasks
        if choice == "1":
            if not tasks:
                print("\nNo tasks in the list.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        # Add task
        elif choice == "2":
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added!")

        # Remove task
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter task number to remove: ")) - 1
                removed = tasks.pop(index)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("Invalid task number.")

        # Edit task
        elif choice == "4":
            if not tasks:
                print("No tasks to edit.")
                continue
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter task number to edit: ")) - 1
                new_text = input("Enter new task text: ")
                tasks[index] = new_text
                print("Task updated!")
            except (ValueError, IndexError):
                print("Invalid task number.")

        # Exit
        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
