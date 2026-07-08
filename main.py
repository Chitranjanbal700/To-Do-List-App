import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({
        "task": task,
        "done": False
    })
    save_tasks(tasks)
    print("✅ Task added successfully!")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n------ TO-DO LIST ------")
    for i, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task["done"] else "❌ Pending"
        print(f"{i}. {task['task']} [{status}]")
    print()

# Mark task complete
def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("🎉 Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑 '{removed['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n====== TO-DO LIST APP ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()