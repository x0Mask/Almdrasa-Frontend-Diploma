"""This is a refactoring version of my code with documentation."""


"""
This is a simple todo list script.

This script allows users to manage a todo list by performing actions such as adding tasks, listing existing tasks,
removing tasks, and exiting the script.

Functions:
- add_task(todo_list): Adds a task to the todo list.
- list_tasks(todo_list): Displays the tasks in the todo list.
- remove_task(todo_list): Removes a task from the todo list.
- todo_list_script(): Manages user interaction and task operations.
"""

def add_task(todo_list):
    """
    Add a task to the todo list.

    Args:
    - todo_list (list): The list of tasks.

    Returns:
    None
    """
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added.")

def list_tasks(todo_list):
    """
    Display the tasks in the todo list.

    Args:
    - todo_list (list): The list of tasks.

    Returns:
    None
    """
    if not todo_list:
        print("No tasks to display.")
    else:
        for task in todo_list:
            print(task)

def remove_task(todo_list):
    """
    Remove a task from the todo list.

    Args:
    - todo_list (list): The list of tasks.

    Returns:
    None
    """
    if not todo_list:
        print("No tasks to remove.")
    else:
        task = input("Enter the task: ")
        if task in todo_list:
            todo_list.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")

def todo_list_script():
    """
    Main function for the todo list script.
    Manages user interaction and task operations.
    """
    todo_list = []

    while True:
        user_action = input("Enter the command (add, list, remove, exit): ")

        if user_action == "add":
            add_task(todo_list)
        elif user_action == "list":
            list_tasks(todo_list)
        elif user_action == "remove":
            remove_task(todo_list)
        elif user_action == "exit":
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    print("This is a todo list script")
    todo_list_script()
