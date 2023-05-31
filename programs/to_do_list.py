""" _summary_

    _extended_summary_
"""

import json
import time


def load_todo_list():
    try:
        with open(
            "/workspaces/python-practice/programs/todo_list.json", "r", encoding="utf-8"
        ) as file:
            to_do_list = json.load(file)
            return to_do_list
    except FileNotFoundError as e:
        print("File was not found: ", e)
        return {}


TODO_LIST = load_todo_list()


def add_task():
    while True:
        print("Add a task:")
        task = input(">>> ")

        if task in TODO_LIST:
            print("Task already exists. Exiting...")
            break

        due_date = "N/A"
        priority_level = "N/A"

        print("Do you want to add a due date? (Y/N)")
        due_confirmation = input(">>> ").lower()

        if due_confirmation == "y":
            print("Enter the due date:")
            due_date = input(">>> ")

        print("Do you want to add a priority level? (Y/N)")
        priority_confirmation = input(">>> ").lower()

        if priority_confirmation == "y":
            print("Enter the priority level:")
            priority_level = input(">>> ")

        TODO_LIST[task] = {
            "task": task.capitalize(),
            "due_date": due_date,
            "priority_level": priority_level,
        }

        print("Do you have any other fields you want to add? (Y/N)")
        field_confirmation = input(">>> ").lower()

        while field_confirmation == "y":
            print("Enter the name of the field:")
            field = input(">>> ")
            print("Enter the value of the field:")
            field_value = input(">>> ")
            TODO_LIST[task][field] = field_value

            print("Do you have any other fields you want to add? (Y/N)")
            field_confirmation = input(">>> ").lower()

        print("Task Added...")
        print("Task Details:")
        print(f"Details: {task.capitalize()}")
        print(f"Due Date: {due_date}")
        print(f"Priority: {priority_level.capitalize()}")

        for field, value in TODO_LIST[task].items():
            if field not in ["task", "due_date", "priority_level"]:
                print(f"{field.capitalize()}: {value}")
                print("--------------------------")
                print("--------------------------")

        print("Do you want to add another task? (Y/N)")
        task_confirmation = input(">>> ").lower()

        if task_confirmation != "y":
            print("Exiting...")
            break


def delete_task():
    print("Enter the name of the task you want to delete: ")
    name_task = input(">>> ")
    print("Scanning for matches...")
    time.sleep(3)
    if name_task in TODO_LIST:
        print("Found matches...")
        print("Deleting Task now...")
        del TODO_LIST[name_task]
        print(f"'{name_task}' has been deleted.")
    else:
        print("Scan turned out empty...")


def display_tasks():
    print("Your Tasks: ")
    sorted_tasks = sorted(
        TODO_LIST.values(),
        key=lambda task: {"high": 0, "medium": 1, "Low": 2}[task["priority_level"]],
    )
    for task in sorted_tasks:
        print(f"Details: {task['task'].capitalize()}")
        print(f"Due Date: {task['due_date']}")
        print(f"Priority: {task['priority_level'].capitalize()}")
        for field, value in task.items():
            if field not in ["task", "due_date", "priority_level"]:
                print(f"{field.capitalize()}: {value}")
        print("--------------------------")


def save_tasks():
    with open(
        "/workspaces/python-practice/programs/todo_list.json", "w", encoding="utf-8"
    ) as r:
        json.dump(TODO_LIST, r)


todo_list_message = """
      Choose an option from the ones below.
      (1) Add a task.
      (2) Print the task list.
      (3) Delete a Task
      

    (4) Exit
"""
print("Hello. Welcome to To Do List..")
print(todo_list_message)
while True:
    choice = input(">>> ")
    if choice == "1":
        add_task()
        time.sleep(4)
        print(todo_list_message)
    elif choice == "2":
        display_tasks()
        time.sleep(4)
        print(todo_list_message)
    elif choice == "3":
        delete_task()
        time.sleep(3)
        print(todo_list_message)
    elif choice == "4":
        print("Okay! Thank you for using this..")
        save_tasks()
        break
    else:
        print("That was not a valid option.. Exiting...")
        save_tasks()
        break
