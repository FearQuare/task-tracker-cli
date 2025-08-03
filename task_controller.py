from pathlib import Path
import json

from task import Task

def fetch_tasks(path, list):
    """Fetches the tasks from a tasks.json to task list."""
    tasks_json = path.read_text()
    tasks = json.loads(tasks_json)
    for task in tasks:
        list.append(task)

def create_task(task_name, task_status):
    """Creating new task."""

    # Fetching the tasks.json file.
    path = Path('tasks.json')

    task_list = []
    id = 1

    if path.exists():
        fetch_tasks(path, task_list)
        id = task_list[-1]["id"]
        id = id + 1

    # Creating the task instance.
    task = Task(id, task_name, task_status)
    
    # Registering the new task to the tasks.json file.
    new_task = task.to_dict()
    task_list.append(new_task)
    contents = json.dumps(task_list)
    path.write_text(contents)
    print(task.get_name(), "task created.")