"""This is a todo list script"""

todo_list = []


while True:
    user_action = input("Enter the command (add, list, remove, exit): ")

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
    elif user_action == "exit":
        break
    else:
        print("Invalid command.")
