tasks = []  # Empty list to store tasks

def list_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ").strip()  # .strip() removes spaces at start/end
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
    except ValueError:  # handles when user inputs text instead of a number
        print("Please, enter a valid number.")

def save_tasks_to_file():
    try:
        with open("tasks.txt", "w") as file:  # "w" means write mode
            for task in tasks:
                file.write(task + "\n")
        print("Tasks saved to 'tasks.txt'.")
    except Exception as e:  # catches any possible error
        print(f"An error occurred while saving tasks: {e}")

def load_tasks_from_file():
    try:
        with open("tasks.txt", "r") as file:  # "r" means read mode
            global tasks  # tells Python we want to modify the tasks list we defined at the top
            tasks = [line.strip() for line in file.readlines()]  # reads each line from file
        print("Tasks loaded from 'tasks.txt'.")
    except FileNotFoundError:
        print("No saved tasks found. Start by adding new tasks.")
    except Exception as e:
        print(f"An error occurred while loading tasks: {e}")

def main():
    while True:
        print("\nWelcome to your Task Manager!")
        print("1. Show me my tasks")
        print("2. Add a new task")
        print("3. Remove a task")
        print("4. Save tasks to file")
        print("5. Load tasks from file")
        print("6. Exit the manager")
        choice = input("What's your choice? ").strip()

        if choice == '1':
            list_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            save_tasks_to_file()
        elif choice == '5':
            load_tasks_from_file()
        elif choice == '6':
            print("Goodbye! See you next time!")
            break
        else:
            print("Oops! That's not a valid option. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()