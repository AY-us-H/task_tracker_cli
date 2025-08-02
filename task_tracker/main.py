import task_manager

def show_menu():
    print("\n--- Task Tracker CLI ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Change status of a Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter description (optional): ")
        due_date = input("Enter due date (DD-MM-YYYY format): ")
        task_manager.add_tasks(title, description)
    elif choice == "2":
        task_manager.list_tasks()
    elif choice == "3":
        try:
            task_id = int(input("Enter task ID to mark as completed: "))
            task_manager.mark_task_completed(task_id)
        except ValueError:
            print("Please enter valid ID.")
    elif choice == "4":
        try:
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        except ValueError:
            print("Please enter valid ID")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")