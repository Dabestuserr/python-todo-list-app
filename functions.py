from task import Task

def add_task(task_list,task):
    new_task = Task(task)
    task_list.append(new_task)
    print(f"The Task: {new_task.description} has been added to the list!")

def view_list(task_list):
    if len(task_list) != 0:
        print("Currently the list is: ")
        for i, task in enumerate(task_list):
            if task.status == "complete":
                print(f"{i + 1}. [X] {task.description}")
            else:
                print(f"{i + 1}. [] {task.description}")
    else:
        print("List is Empty!")

def mark_complete(task_list, num):
    try:
        if num > 0:
            try:
                task = task_list[num-1]
                task.status = "complete"
                print(f"Number: {num}, Task: {task.description}, has been completed!")
                return
            except IndexError:
                print(f"Number: {num} is not in the list! Please provide a valid number from the list!")
        else:
            print(f"Number: {num} has to be greater than 0!")
            return
    except TypeError or IndexError:
        print(f"Number: {num} is not a valid INTEGER! Please provide a valid number from the list! Ex. 1,2,3,4,5")

def task_remove(task_list, num):
    try:
        if num > 0:
            try:
                task = task_list.pop(num-1)
                print(f"Number: {num}, Task: {task.description}, has been removed from the list!")
                return
            except IndexError:
                print(f"Number: {num} is not in the list! Please provide a valid number from the list!")
        else:
            print(f"Number: {num} has to be greater than 0!")
            return
    except TypeError:
        print(f"Number: {num} is not a valid INTEGER! Please provide a valid number from the list! Ex. 1,2,3,4,5")

