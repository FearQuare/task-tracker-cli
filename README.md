# Task Tracker CLI

A simple command-line tool for tracking your tasks. You can add, update, delete, and list tasks, as well as mark them as in-progress or done. Tasks are stored in a local JSON file for persistence.

## Features
- Add new tasks
- Update task descriptions
- Delete tasks
- Mark tasks as in-progress or done
- List tasks, optionally filtered by status

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/FearQuare/task-tracker-cli.git
   cd task-tracker-cli
   ```
2. Make sure you have Python 3.7+ installed.
3. (Optional) Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install any required dependencies (if any):
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the CLI using:
```sh
python task_tracker.py <command> [options]
```

### Commands

#### Add a new task
```sh
python task_tracker.py add "Buy groceries"
```

#### Update a task's description
```sh
python task_tracker.py update 1 "Buy groceries and cook dinner"
```

#### Delete a task
```sh
python task_tracker.py delete 1
```

#### Mark a task as in-progress
```sh
python task_tracker.py mark-in-progress 2
```

#### Mark a task as done
```sh
python task_tracker.py mark-done 2
```

#### List all tasks
```sh
python task_tracker.py list
```

#### List tasks by status
```sh
python task_tracker.py list done
python task_tracker.py list todo
python task_tracker.py list in-progress
```

## Example Session
```
$ python task_tracker.py add "Write documentation"
Write documentation task created.

$ python task_tracker.py add "Review pull requests"
Review pull requests task created.

$ python task_tracker.py list
ID    | Task Name                          | Status      | Create Date                | Update Date                
------------------------------------------------------------------------------------------------------------------------
1     | Write documentation                | to-do       | 2025-08-06T12:34:56        | 2025-08-06T12:34:56        
2     | Review pull requests               | to-do       | 2025-08-06T12:35:10        | 2025-08-06T12:35:10        

$ python task_tracker.py mark-in-progress 1
Task 1 marked as in-progress.

$ python task_tracker.py list in-progress
ID    | Task Name                          | Status      | Create Date                | Update Date                
------------------------------------------------------------------------------------------------------------------------
1     | Write documentation                | in progress | 2025-08-06T12:34:56        | 2025-08-06T12:36:00        

$ python task_tracker.py mark-done 1
Task 1 marked as done.

$ python task_tracker.py list done
ID    | Task Name                          | Status      | Create Date                | Update Date                
------------------------------------------------------------------------------------------------------------------------
1     | Write documentation                | done        | 2025-08-06T12:34:56        | 2025-08-06T12:37:15        
```

## Notes
- All tasks are stored in `tasks.json` in the project directory.
- Task IDs are auto-incremented.
- Status options: `to-do`, `in progress`, `done`.

## Contributing
Feel free to open issues or submit pull requests for improvements!

## License
MIT
# task-tracker-cli
https://roadmap.sh/projects/task-tracker
