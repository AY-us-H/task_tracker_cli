import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  #this tells python to look in the parent directory, where the complete folder is located, when seatching for modules
from complete import storage
from datetime import datetime

# Function to add tasks
def add_tasks(title, description="", due_date=""):
    tasks = storage.load_tasks()
    task_id = len(tasks) + 1

    # validating due_date formate
    try:
        if due_date:
            datetime.strptime(due_date, "%d-%m-%Y")
    except ValueError:
        print("Ivalid date format. Use DD-MM-YYYY format.")
        return

    task = {
        "id" : task_id,
        "title" : title,
        "description" : description,
        "status" : "Pending",
        "due_date": due_date
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

    for task in tasks:
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

def delete_task(task_id):
    tasks = storage.load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == len(updated_tasks):
        print("Task not found")
        return
    # Reassign IDs
    for index, task in enumerate(updated_tasks):
        task["id"] = index + 1
    storage.save_tasks(updated_tasks)
    print("Task deleted Successfully")
