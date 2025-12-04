#todo list
# Simple To-Do List Program

todo_list = []

#Menu
def show_menu():
    print(" TO-DO LIST MENU ")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Remove Task")
    print("5. Exit")

# View tasks
def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    if task.strip()=="":
        print("wala man task oi!!")
    else:
        todo_list.append(task)
        print("Task added!")


def edit_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("\nEnter task number to edit: "))
            if 1 <= task_num <= len(todo_list):
                new_task = input("Enter new task text: ")
                todo_list[task_num - 1] = new_task
                print("Task updated!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")