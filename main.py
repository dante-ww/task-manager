tasks = []  # List to store tasks

def list_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ").strip()
    if not task:
        print("Task cannot be empty. Please enter a valid task.")
    else:
        tasks.append(task)
        print(f"Task '{task}' added.")

def delete_task():
    if not tasks:
        print("There are no tasks to remove.")
        return

    list_tasks()
    try:
        task_num = int(input("Enter the number of the task you want to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print(f"Invalid number. Please enter a number between 1 and {len(tasks)}.")
    except ValueError:
        print("Please, enter a valid number.")

def main():
    while True:
        print("\nWelcome to your Task Manager!")
        print("1. Show me my tasks")
        print("2. Add a new task")
        print("3. Remove a task")
        print("4. Exit the manager")
        choice = input("What's your choice? ").strip()

        if choice == '1':
            list_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Goodbye! See you next time!")
            break
        else:
            print("Oops! That's not a valid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()