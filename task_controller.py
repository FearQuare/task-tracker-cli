from pathlib import Path
import json

from task import Task

path = Path('tasks.json')

def fetch_tasks(path, list):
    """Fetches the tasks from a tasks.json to task list."""
    tasks_json = path.read_text()
    tasks = json.loads(tasks_json)
    for task in tasks:
        list.append(task)

def list_tasks():
    task_list = []
    if path.exists():
        fetch_tasks(path, task_list)
        if task_list:
            print(f"{'ID':<5} | {'Task Name':<35} | {'Status':<12}")
            print("-" * 60)
            for task in task_list:
                print(f"{task['id']:<5} | {task['name']:<35} | {task['status']:<12}")
        else:
            print("No tasks found.")
    else:
        print("No tasks.json file found.")


def create_task(task_name, task_status):
    """Creating new task."""
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