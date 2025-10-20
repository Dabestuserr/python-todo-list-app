#TODO LIST APP

tasks = {}

def add_task(task_list,task):
    task_list[task] = "incomplete"
    print(f"The Task: {task} has been added to the list!")

def view_list(task_list):
    if len(task_list) != 0:
        print("Currently the list is: ")
        for i, (task,value) in enumerate(task_list.items()):
            if value == "complete":
                print(f"{i + 1}. [X] {task}")
            else:
                print(f"{i + 1}. [] {task}")
    else:
        print("List is Empty!")

def mark_complete(task_list, num):
    if num > 0:
        for i, (task, value) in enumerate(task_list.items()):
            if i+1 == num:
                task_list[task] = "complete"
                print(f"Number: {num}, Task: {task}, has been completed!")
                return
    else:
        print(f"Number: {num} has to be greater than 0!")
        return
    print(f"Number: {num} is not in the list! Please provide a valid number from the list!")

def task_remove(task_list, num):
    if num > 0:
        for i, (task, value) in enumerate(task_list.items()):
            if i+1 == num:
                task_list.pop(task)
                print(f"Number: {num}, Task: {task}, has been removed from the list!")
                return
    else:
        print(f"Number: {num} has to be greater than 0!")
        return
    print(f"Number: {num} is not in the list! Please provide a valid number from the list!")


print("Welcome to your To-Do List!\n"
        "---------------------------\n"
        "1. Add a new task\n"
        "2. View all tasks\n"
        "3. Mark a task as complete\n"
        "4. Remove a task\n"
        "5. Exit\n")
user_command = input("What would you like to do today?: ")
while user_command != "5":
    if int(user_command) in range(1,6):
        if user_command == "1":
            task = input("What task would you like to add?: ")
            add_task(tasks, task)
        elif user_command == "2":
            view_list(tasks)
        elif user_command == "3":
            task = input("What task would you like to complete?: ")
            mark_complete(tasks, int(task))
        elif user_command == "4":
            task = input("What task would you like to remove? Provide a Number!: ")
            task_remove(tasks, int(task))
    else:
        print("Please provide a number between 1 and 5!")
    user_command = input("What would you like to do today?: ")
print("Goodbye!")
