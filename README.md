# Task Manager

A simple command-line task manager built with Python that helps you organize your daily tasks.

## Features
- Add and remove tasks with confirmation
- Mark tasks as completed with [DONE] status
- Save tasks to file with timestamps
- Load tasks from previous sessions
- Input validation and error handling
- Task limit protection (50 tasks maximum)
- Task length validation (100 characters max)

## Requirements
- Python 3.x
- Standard library packages:
  - os
  - datetime

## Installation
1. Clone or download this repository
2. Navigate to the project directory
3. Run the program using Python

## Usage
Start the program:
```bash
python main.py
```

### Available Commands
1. Show tasks - Display all your current tasks
2. Add task - Create a new task
3. Remove task - Delete an existing task
4. Mark as completed - Mark a task as done
5. Save to file - Save your tasks to tasks.txt
6. Load from file - Load previously saved tasks
7. Exit - Close the program

### Examples
- Adding a task: Enter task description when prompted
- Removing a task: Select task number and confirm deletion
- Marking as complete: Select task number to mark as [DONE]

## File Storage
- Tasks are stored in 'tasks.txt'
- UTF-8 encoding is used
- Each task is stored on a new line
- Timestamps are included with each task

## Author
Dante

## License
This project is open source and available under the MIT License.
