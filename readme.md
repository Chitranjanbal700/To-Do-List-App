## Python To-Do List App

A simple command-line To-Do List application built with Python. This project allows users to manage daily tasks by adding, viewing, completing, and deleting tasks. All tasks are stored in a JSON file, so they remain available even after the program is closed.

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Automatically save tasks in a JSON file
* Data persists after restarting the application

## Project Structure

```
todo-list-app/
│
├── todo.py          # Main Python program
├── tasks.json       # Stores all tasks (created automatically)
└── README.md        # Project documentation
```

## Requirements

* Python 3.8 or above

No external libraries are required.

## Menu

```
====== TO-DO LIST APP ======

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
```

## Data Storage

Tasks are stored in a file named `tasks.json`.

Example:

```json
[
    {
        "task": "Complete Python project",
        "done": false
    },
    {
        "task": "Read a book",
        "done": true
    }
]
```

## Future Improvements

* Edit existing tasks
* Search tasks
* Task priorities (High, Medium, Low)
* Due dates and reminders
* GUI using Tkinter
* Dark mode
* Export tasks to CSV or PDF
