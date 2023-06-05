import json
import os

def load_tasks():
    if os.path.exists('tasks.json') and os.path.getsize('tasks.json') > 0:
        with open('tasks.json') as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task():
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    task = {'name': name, 'description': description, 'status': 'Incomplete'}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks):
            print(f"Task #{index + 1}:")
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print()

def update_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("Enter the task number to update: ")) - 1
            if 0 <= task_number < len(tasks):
                task = tasks[task_number]
                new_status = input("Enter the new status (Incomplete/Complete): ")
                task['status'] = new_status
                save_tasks(tasks)
                print("Task updated successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input.")
    else:
        print("No tasks found.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_number < len(tasks):
                del tasks[task_number]
                save_tasks(tasks)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input.")
    else:
        print("No tasks found.")

def print_menu():
    print("Command-Line Task Management Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

tasks = load_tasks()

while True:
    print_menu()
    choice = input("Enter your choice (1-5): ")
    print()

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Task Management Application!")