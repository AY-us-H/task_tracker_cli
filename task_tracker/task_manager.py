import complete.storage

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

def mark_task_completed(task_id):
    tasks = complete.storage.load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            complete.storage.save_tasks(tasks)
            print("Task marked as completed")
            return
    print("Task not found")