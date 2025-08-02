# This block of code handles the reading from and writing to tasks.json file

import json
import os

TASK_FILE = "tasks.json"

"""
1. check if the file exists
2. open the file in read mode
3. load the tasks from the file and return them as list
4. if the file does not exist, return an empty list
"""
def load_tasks():
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
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)