import os
from datetime import datetime

tasks = []
MAX_TASKS = 50
MAX_TASK_LENGTH = 100

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def list_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    if len(tasks) >= MAX_TASKS:
        print(f"Task limit reached ({MAX_TASKS}). Please remove some tasks first.")
        return

    task = input("Enter a new task: ").strip()  # .strip() removes spaces at start/end
    if not task:
        print("Task cannot be empty. Please enter a valid task.")
    elif len(task) > MAX_TASK_LENGTH:
        print(f"Task is too long. Maximum length is {MAX_TASK_LENGTH} characters.")
    else:
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        tasks.append(f"[{date}] {task}")
        print(f"Task '{task}' added.")

def delete_task():
    if not tasks:
        print("There are no tasks to remove.")
        return

    list_tasks()
    try:
        task_num = int(input("Enter the number of the task you want to remove: "))
        if 1 <= task_num <= len(tasks):
            confirm = input(f"Are you sure you want to delete '{tasks[task_num-1]}'? (y/n): ").lower()
            if confirm == 'y':
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Task deletion cancelled.")
        else:
            print(f"Invalid number. Please enter a number between 1 and {len(tasks)}.")
    except ValueError:  # handles when user inputs text instead of a number
        print("Please, enter a valid number.")

def mark_completed():
    if not tasks:
        print("No tasks to mark as completed.")
        return
    list_tasks()
    try:
        task_num = int(input("Enter the number of the completed task: "))
        if 1 <= task_num <= len(tasks):
            if "[DONE]" in tasks[task_num-1]:
                print("This task is already marked as completed!")
                return
            tasks[task_num-1] = f"[DONE] {tasks[task_num-1]}"
            print("Task marked as completed!")
    except ValueError:
        print("Please enter a valid number.")

def save_tasks_to_file():
    try:
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Tasks saved to 'tasks.txt'.")
    except Exception as e:
        print(f"An error occurred while saving tasks: {e}")

def load_tasks_from_file():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            global tasks
            tasks = [line.strip() for line in file.readlines()]
        print("Tasks loaded from 'tasks.txt'.")
    except FileNotFoundError:
        print("No saved tasks found. Start by adding new tasks.")
    except Exception as e:
        print(f"An error occurred while loading tasks: {e}")

def main():
    clear_screen()
    print("="*50)
    print("Welcome to Task Manager v1.0".center(50))
    print("A simple task manager for your daily needs".center(50))
    print("="*50)
    input("Press Enter to continue...")

    while True:
        clear_screen()
        print("\nWelcome to your Task Manager!")
        print("1. Show me my tasks")
        print("2. Add a new task")
        print("3. Remove a task")
        print("4. Mark task as completed")
        print("5. Save tasks to file")
        print("6. Load tasks from file")
        print("7. Exit the manager")
        choice = input("What's your choice? ").strip()

        if choice == '1':
            list_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            mark_completed()
        elif choice == '5':
            save_tasks_to_file()
        elif choice == '6':
            load_tasks_from_file()
        elif choice == '7':
            print("Goodbye! See you next time!")
            break
        else:
            print("Oops! That's not a valid option. Please choose between 1 and 7.")

if __name__ == "__main__":
    main()