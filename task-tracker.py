def menu():
    display_text = """Menu:
    1. List your current tasks and their status.
    2. Create a task.
    3. Update a task.
    4. Delete a task.
    5. List by the status (done, todo, in-progress).\n
    """
    print(display_text)
if __name__=="__main__":
    print("Welcome to Task-Tracker!\n")
    menu()