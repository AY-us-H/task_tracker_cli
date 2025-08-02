import complete.storage

# Function to add tasks
def add_tasks(title, description=""):
    tasks = complete.storage.load_tasks()
    task_id = len(tasks) + 1
    task = {
        "id" : task_id,
        "title" : title,
        "description" : description,
        "status" : "Pending"
    }
    tasks.append(task)
    complete.storage.save_tasks(tasks)
    print("Task added successfully")

# Function to Show tasks
def list_tasks():
    tasks = complete.storage.load_tasks()
    if not tasks:
        print("No tasks found")
        return
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        if task['description']:
            print(f"Desscription: {task['description']}")
        print(f"Status: {task['status']}")
        print("-" * 20)

# Function to mark task as completed
def mark_task_completed(task_id):
    tasks = complete.storage.load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            complete.storage.save_tasks(tasks)
            print("Task marked as completed")
            return
    print("Task not found")

def delete_task(task_id):
    tasks = complete.storage.load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == len(updated_tasks):
        print("Task not found")
        return
    # Reassign IDs
    for index, task in enumerate(updated_tasks):
        task["id"] = index + 1
    complete.storage.save_tasks(updated_tasks)
    print("Task deleted Successfully")
