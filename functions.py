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

