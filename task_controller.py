from pathlib import Path
from datetime import datetime
import json

from task import Task

path = Path('tasks.json')

def fetch_tasks(path, task_list):
    """Fetches the tasks from a tasks.json to task list."""
    tasks_json = path.read_text()
    tasks = json.loads(tasks_json)
    for task in tasks:
        task_list.append(task)

def register_tasks(task_list):
    contents = json.dumps(task_list)
    path.write_text(contents)

def list_tasks(status):
    task_list = []
    if path.exists():
        fetch_tasks(path, task_list)
        if task_list:
            print(f"{'ID':<5} | {'Task Name':<35} | {'Status':<12} | {'Create Date':<26} | {'Update Date':<26}" )
            print("-" * 120)
            for task in task_list:
                if status == 'todo':
                    if task['status'] == 'to-do':
                        print(f"{task['id']:<5} | {task['name']:<35} | {task['status']:<12} | {task['create-date']:<15} | {task['update-date']:<15}")
                elif status == 'in-progress':
                    if task['status'] == 'in progress':
                        print(f"{task['id']:<5} | {task['name']:<35} | {task['status']:<12} | {task['create-date']:<15} | {task['update-date']:<15}")
                elif status == 'done':
                    if task['status'] == 'done':
                        print(f"{task['id']:<5} | {task['name']:<35} | {task['status']:<12} | {task['create-date']:<15} | {task['update-date']:<15}")
                else:
                    print(f"{task['id']:<5} | {task['name']:<35} | {task['status']:<12} | {task['create-date']:<15} | {task['update-date']:<15}")
        else:
            print("No tasks found.")
    else:
        print("No tasks.json file found.")

def create_task(task_name):
    """Creating new task."""
    task_list = []
    id = 1

    if path.exists():
        fetch_tasks(path, task_list)
        id = task_list[-1]["id"]
        id = id + 1

    # Creating the task instance.
    task = Task(id, task_name, "to-do", datetime.now().isoformat(), datetime.now().isoformat())
    
    # Registering the new task to the tasks.json file.
    new_task = task.to_dict()
    task_list.append(new_task)
    register_tasks(task_list)

def update_task(task_id, task_name):
    tasks = []
    if path.exists():
        fetch_tasks(path, tasks)
    else:
        print("No tasks.json file found.")
    
    for task in tasks:
        if task['id'] == int(task_id):
            task['name'] = task_name
            task['update-date'] = datetime.now().isoformat()
            register_tasks(tasks)

def delete_task(task_id):
    tasks = []
    if path.exists():
        fetch_tasks(path, tasks)
        # Remove tasks with matching id
        tasks = [task for task in tasks if task['id'] != int(task_id)]
        register_tasks(tasks)
        print(f"Task {task_id} deleted.")
    else:
        print("No tasks.json file found.")

def mark_in_progress(task_id):
    tasks = []
    if path.exists():
        fetch_tasks(path, tasks)
    else:
        print("No tasks.json file found.")
    
    for task in tasks:
        if task['id'] == int(task_id):
            task['status'] = "in progress"
            task['update-date'] = datetime.now().isoformat()
            register_tasks(tasks)

def mark_done(task_id):
    tasks = []
    if path.exists():
        fetch_tasks(path, tasks)
    else:
        print("No tasks.json file found.")
    
    for task in tasks:
        if task['id'] == int(task_id):
            task['status'] = "done"
            task['update-date'] = datetime.now().isoformat()
            register_tasks(tasks)