# Task Tracker CLI Application

A simple command-line interface application for managing daily tasks. This application helps you keep track of what needs to be done, mark tasks as completed, and maintain an organized list of your responsibilities. The tasks are also sorted according to date.

## What This Application Does

The Task Tracker is designed to be straightforward. It lets you add new tasks with titles and optional descriptions, view all your current tasks, mark them as completed, and remove tasks you no longer need. All your task data is automatically saved to a JSON file.

## How It Works

The application is built with a modular approach that separates different concerns:

- **Main Interface**: The main.py file handles the user interface and menu system
- **Task Management**: The task_manager.py file contains all the logic for adding, listing, updating, and deleting tasks
- **Data Storage**: The storage.py file manages reading from and writing to the JSON file where your tasks are saved

This separation makes the code easier to understand and maintain. When you add a task, the application creates a new entry with a unique ID, title, description, and status. The status starts as "Pending" and can be changed to "Completed" when you finish the task.

## Features

**Add Tasks**: Create new tasks with a title and optional description. The application automatically assigns a unique ID to each task.

**View Tasks**: See all your current tasks displayed with their ID, title, description, and current status.

**Mark as Completed**: Change the status of any task from "Pending" to "Completed" by entering its ID.

**Delete Tasks**: Remove tasks you no longer need. The application will automatically reassign IDs to keep them sequential.

**Persistent Storage**: All your tasks are saved to a JSON file in the file directory, so your data persists between sessions.

## How to Run the Application

To get started with the Task Tracker, follow these simple steps:

1. Make sure you have Python installed on your computer (Python 3.6 or higher recommended)

2. Open your terminal or command prompt

3. Navigate to the project directory where you have the task_tracker folder

4. Run the application by typing:
   ```
   python task_tracker/main.py
   ```

5. The application will start and show you a menu with five options:
   - Option 1: Add a new task
   - Option 2: View all your tasks
   - Option 3: Mark a task as completed
   - Option 4: Delete a task
   - Option 5: Exit the application

6. Simply enter the number corresponding to what you want to do and follow the prompts

## Project Structure

The application is organized into several directories and files:

- **task_tracker/main.py**: The main entry point that runs the application and handles user interaction
- **task_tracker/task_manager.py**: Contains all the functions for managing tasks (add, list, update, delete)
- **complete/storage.py**: Handles reading from and writing to the JSON file where tasks are stored
- **file/tasks.json**: The JSON file where all your task data is saved
- **complete/__init__.py**: Makes the complete directory a Python package

## Data Storage

Your tasks are automatically saved to a file called tasks.json in the file directory. This file is created automatically when you add your first task. The data is stored in JSON format, which makes it easy to read and understand. Each task entry includes an ID, title, description, and status.

## Example Usage

When you run the application, you'll see a menu like this:

```
--- Task Tracker CLI ---
1. Add Task
2. Show Tasks
3. Change status of a Task
4. Delete Task
5. Exit
Enter your choice (1-5):
```

To add a task, select option 1 and enter the task title and description when prompted. To view all your tasks, select option 2. The application will show each task with its details clearly formatted.

## Technical Details

The application uses Python's built-in modules for file handling and JSON processing. It creates the necessary directories automatically if they don't exist, so you don't need to worry about setting up the file structure manually. The import system is configured to work properly regardless of which directory you run the application from.

This Task Tracker is perfect for anyone who wants a simple, no-frills way to manage their daily tasks without the complexity of larger project management tools.
