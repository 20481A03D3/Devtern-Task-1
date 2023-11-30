import json
from datetime import datetime

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['title']} - {task['date']}")

def add_task(tasks, title):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({'title': title, 'date': timestamp})
    print("Task added successfully.")

def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task['title']}' removed successfully.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            title = input("Enter task title: ")
            add_task(tasks, title)
        elif choice == '3':
            index = int(input("Enter task index to remove: "))
            remove_task(tasks, index)
        elif choice == '4':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
