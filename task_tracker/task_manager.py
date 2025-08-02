import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  #this tells python to look in the parent directory, where the complete folder is located, when seatching for modules
from complete import storage
from datetime import datetime

# Function to add tasks
def add_tasks(title, description="", due_date=""):
    tasks = storage.load_tasks()
    task_id = len(tasks) + 1

    # validating due_date format
    if due_date.strip():  # Only validate if due_date is not empty or just whitespace
        try:
            datetime.strptime(due_date.strip(), "%d-%m-%Y")  #check if the due_date string matches the format
        except ValueError:
            print("Invalid date format. Use DD-MM-YYYY format.")
            return

    task = {
        "id" : task_id,
        "title" : title,
        "description" : description,
        "status" : "Pending",
        "due_date": due_date.strip() if due_date.strip() else ""
    }
    tasks.append(task)
    storage.save_tasks(tasks)
    print("Task added successfully")

# Function to Show tasks
def list_tasks():
    tasks = storage.load_tasks()
    if not tasks:
        print("No tasks found")
        return
    
    # sortig tasks by due_date if available
    def sort_tasks(task):
        return task.get("due_date") or "31-12-9999" #tasks withput due_date will go last

    # sort tasks by due date
    sorted_tasks = sorted(tasks, key=sort_tasks)
    
    for task in sorted_tasks:
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        if task['description']:
            print(f"Desscription: {task['description']}")
        print(f"Status: {task['status']}")
        if task.get("due_date"):
            print(f"Due Date: {task['due_date']}")
        print("-" * 20)

# Function to mark task as completed
def mark_task_completed(task_id):
    tasks = storage.load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            storage.save_tasks(tasks)
            print("Task marked as completed")
            return
    print("Task not found")

# function to delete a task using task_id
def delete_task(task_id):
    tasks = storage.load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == len(updated_tasks):
        print("Task not found")
        return
    # reassign IDs
    for index, task in enumerate(updated_tasks):
        task["id"] = index + 1
    storage.save_tasks(updated_tasks)
    print("Task deleted Successfully")
