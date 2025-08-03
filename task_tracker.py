from task_controller import create_task

def menu():
    display_text = """Menu:
    1. List your current tasks and their status.
    2. Create a task.
    3. Update a task.
    4. Delete a task.
    5. List by the status (done, todo, in-progress).\n
    """
    print(display_text)

def creating_task():
    name = input("Name of the task: ")
    status_text = """Select the status of the task:
    1. To-do
    2. Ongoing
    3. Completed
    : """
    status = input(status_text)
    if status == '1':
        create_task(name, "to-do")
    elif status == '2':
        create_task(name, "ongoing")
    elif status == '3':
        create_task(name, "completed")
    else:
        print("Please enter a valid input.")

if __name__=="__main__":
    print("Welcome to Task-Tracker!\n")
    menu()
    decision = input("Please enter the index of the operation you want to run: ")
    if decision == '2':
        creating_task()
    else:
        print("Please enter a valid input.")