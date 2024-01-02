"""This is a todo list script"""

todo_list = []


while True:
    user_action = input("Enter the command (add, list, edit, remove, exit): ")

    if user_action == "add":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added.")
    elif user_action == "list":
        if not todo_list:
            print("No tasks to display.")
        else:
            for task in todo_list:
                print(task)
    elif user_action == "remove":
        if not todo_list:
            print("No tasks to remove.")
        else:
            task = input("Enter the task: ")
            if task in todo_list:
                todo_list.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")
    elif user_action == "edit":
        task = input("Enter the task to edit: ")
        if task in todo_list:
            edit_task = input("Enter the edit: ")
            list_as_string = ' '.join(todo_list)
            new_string = list_as_string.replace(task, edit_task)
            todo_list = new_string.split()
        else:
            print("The task you entered isn't found.")
    elif user_action == "exit":
        break
    else:
        print("Invalid command.")
