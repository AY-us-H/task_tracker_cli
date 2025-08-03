# Task Tracker CLI Application

A simple command-line interface application for managing daily tasks with due date support and timestamps. This application helps you keep track of what needs to be done, mark tasks as completed, and maintain an organized list of your responsibilities. Tasks are automatically sorted by due date for better organization.

## What This Application Does

The Task Tracker is designed to be straightforward and efficient. It lets you add new tasks with titles, optional descriptions, and due dates, view all your current tasks in chronological order, mark them as completed with timestamps, and remove tasks you no longer need. All your task data is automatically saved to a JSON file with persistent sorting.

## Features

### Core Functionality
- **Add Tasks**: Create new tasks with a title, optional description, and due date
- **View Tasks**: See all your current tasks displayed with ID, title, description, status, due date, and creation timestamp
- **Mark as Completed**: Change task status from "Pending" to "Completed" with completion timestamp
- **Delete Tasks**: Remove tasks you no longer need with automatic ID reassignment
- **Persistent Storage**: All tasks saved to JSON file with data persistence between sessions

### Enhanced Features
- **Due Date Support**: Add due dates in DD-MM-YYYY format with validation
- **Automatic Sorting**: Tasks sorted chronologically by due date (tasks without due dates appear last)
- **Timestamps**: Creation and completion timestamps for better task tracking
- **Data Validation**: Input validation for date formats and task IDs
- **Error Handling**: Comprehensive error handling for invalid inputs and missing tasks

## How It Works

The application uses a modular architecture that separates different concerns:

- **Main Interface** (`main.py`): Handles user interface and menu system
- **Task Management** (`task_manager.py`): Contains all logic for adding, listing, updating, and deleting tasks
- **Data Storage** (`storage.py`): Manages reading from and writing to JSON file with automatic sorting

When you add a task, the application creates a new entry with a unique ID, title, description, status, due date, and creation timestamp. Tasks are automatically sorted by due date and saved to the JSON file in the correct order.

## How to Run the Application

### Prerequisites
- Python 3.6 or higher installed on your system

### Running the Application
1. Open your terminal or command prompt
2. Navigate to the project directory
3. Run the application:
   ```bash
   python main.py
   ```
4. Follow the interactive menu prompts

### Menu Options
The application presents a simple menu with five options:
```
--- Task Tracker CLI ---
1. Add Task
2. Show Tasks
3. Change status of a Task
4. Delete Task
5. Exit
```

## Usage Examples

### Adding a Task
```
Enter your choice (1-5): 1
Enter task title: Complete project documentation
Enter description (optional): Write comprehensive README and code comments
Enter due date (DD-MM-YYYY format): 15-08-2025
Task added successfully
```

### Viewing Tasks
```
Enter your choice (1-5): 2
ID: 1
Title: Complete project documentation
Description: Write comprehensive README and code comments
Status: Pending
Due Date: 15-08-2025
Created: 03-08-2025 14:30:25
--------------------
```

### Marking Task as Completed
```
Enter your choice (1-5): 3
Enter task ID to mark as completed: 1
Task marked as completed
```

## Data Storage Format

Tasks are stored in JSON format in `file/tasks.json`:

```json
[
    {
        "id": 1,
        "title": "Complete project documentation",
        "description": "Write comprehensive README and code comments",
        "status": "Pending",
        "due_date": "15-08-2025",
        "created_at": "03-08-2025 14:30:25"
    }
]
```

## Technical Implementation Details

- **Date Parsing**: Uses `datetime.strptime()` for proper chronological sorting
- **Automatic Sorting**: JSON file remains sorted by due date at all times
- **ID Management**: Sequential ID reassignment after deletions
- **Path Resolution**: Dynamic import path configuration for cross-platform compatibility
- **Input Validation**: Comprehensive validation for dates and numeric inputs

## Challenges Faced During Development

### 1. Task Sorting by Due Date

**The Problem**: Initially, tasks were not sorting correctly by due date. The application was treating dates as strings and performing lexicographical (alphabetical) sorting instead of chronological sorting.

**What Went Wrong**: When sorting date strings like "04-05-2025", "05-07-2025", and "06-06-2025", Python was comparing them character by character as strings. This meant "05-07-2025" would come before "06-06-2025" because "05" < "06" as strings, but this didn't reflect the actual chronological order.

**The Solution**: I resolved this by converting date strings to `datetime` objects before sorting. The sorting function now uses `datetime.strptime()` to parse the date strings into proper datetime objects, which can be compared chronologically. I also implemented proper error handling for invalid date formats and ensured tasks without due dates appear last in the sorted list.

### 2. Module Import Errors

**The Problem**: The application was experiencing import errors when trying to access the storage module from different directories, particularly when running the application from various locations in the file system.

**What Went Wrong**: Python couldn't locate the storage module because the import paths weren't properly configured for the project structure. The `task_manager.py` file needed to import from the `complete` directory, but Python wasn't looking in the right places.

**The Solution**: I implemented a dynamic path configuration using `sys.path.append()` to add the parent directory to Python's module search path. This ensures that regardless of where the application is run from, Python can always find the required modules.



These challenges taught me valuable lessons about data type handling, Python import systems, and maintaining data consistency across different layers of an application. Each problem required careful debugging and testing to ensure the solutions worked reliably across different use cases.

## Requirements Fulfilled

**List Tasks**: Display all tasks with ID, title, description, and status  
**Add Task**: Users can add tasks with title and optional description  
**Mark Complete**: Update task status to 'Completed' using task ID  
**Delete Task**: Remove tasks using their ID  
**Data Persistence**: Tasks stored and loaded from local JSON file  
**Due Date Support**: Bonus feature implemented with date validation  
**Sort by Due Date**: Bonus feature implemented with proper chronological sorting  

## Future Enhancements

Potential improvements that could be added:
- Task categories or tags
- Priority levels
- Search and filter functionality
- Task editing capabilities
- Export functionality (CSV, PDF)
- Recurring task support

---

**Note**: This project was developed without the assistance of Large Language Models (LLMs), with all code written independently and challenges solved through research and experimentation.