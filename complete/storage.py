# This block of code handles the reading from and writing to tasks.json file

import json
import os

# Keeping json file under "file" directory
TASK_FILE = os.path.join("file", "tasks.json")

"""
1. check if the file exists
2. open the file in read mode
3. load the tasks from the file and return them as list
4. if the file does not exist, return an empty list
"""
def load_tasks():
    # ensuring the file directory exists
    file_dir = os.path.dirname(TASK_FILE)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:      
            return json.load(file)      
    return []   

"""
1. open the tasks.json file in write mode which overwrites the existing file
2. convert python list of tasks to json format and write it to the file
3. indent the file by 4 spaces
"""
def save_tasks(tasks):
    # ensure the file directory exists
    file_dir = os.path.dirname(TASK_FILE)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)