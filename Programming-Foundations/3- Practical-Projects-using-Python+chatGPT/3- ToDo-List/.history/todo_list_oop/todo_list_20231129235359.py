class TodoList:
    def __init__(self):
        self.todo_list = []

    def add_task(self):
        task = input("Enter the task: ")
        self.todo_list.append(task)
        print("Task added.")

    def list_tasks(self):
        if not self.todo_list:
            print("No tasks to display.")
        else:
            for task in self.todo_list:
                print(task)

    def edit_task(self):
        """
        Edits a task in the todo list.
        """
        task = input("Enter the task to edit: ")
        if task in self.todo_list:
            index = todo_list.index(task)
            new_task = input("Enter the edit: ")
            todo_list[index] = new_task
            print("Task edited successfully.")
        else:
            print("The task you entered isn't found.")


    def remove_task(self):
        if not self.todo_list:
            print("No tasks to remove.")
        else:
            task = input("Enter the task: ")
            if task in self.todo_list:
                self.todo_list.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")

    def todo_list_script(self):
        while True:
            user_action = input("Enter the command (add, list, remove, exit): ")

            if user_action == "add":
                self.add_task()
            elif user_action == "list":
                self.list_tasks()
            elif user_action == "remove":
                self.remove_task()
            elif user_action == "exit":
                break
            else:
                print("Invalid command.")
