# To-Do List Application

tasks = []  # Empty list to store tasks

def show_tasks():
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    """Add a new task."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task():
    """Remove a task by its number."""
    show_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        if 1 <= task_no <= len(tasks):
            removed_task = tasks.pop(task_no - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting... Have a great day!")
        break
    else:
        print("Invalid choice! Please try again.")
