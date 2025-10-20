#TODO LIST APP
import functions
from task import Task

tasks = []

print(tasks)
functions.add_task(tasks,"Orange")
functions.view_list(tasks)
functions.add_task(tasks,"Banana")
functions.view_list(tasks)
functions.mark_complete(tasks, 1)
functions.view_list(tasks)
functions.task_remove(tasks, 1)
functions.view_list(tasks)

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
            functions.add_task(tasks, task)
        elif user_command == "2":
            functions.view_list(tasks)
        elif user_command == "3":
            task = input("What task would you like to complete?: ")
            functions.mark_complete(tasks, int(task))
        elif user_command == "4":
            task = input("What task would you like to remove? Provide a Number!: ")
            functions.task_remove(tasks, int(task))
    else:
        print("Please provide a number between 1 and 5!")
    user_command = input("What would you like to do today?: ")
print("Goodbye!")
