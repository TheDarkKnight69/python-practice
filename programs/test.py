""" _summary_

    _extended_summary_
"""

import json
import time


def load_todo_list():
    try:
        with open("todo_list.json", "r", encoding="utf-8") as file:
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
            "task": task,
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
        print(f"Details: {task}")
        print(f"Due Date: {due_date}")
        print(f"Priority: {priority_level}")

        for field, value in TODO_LIST[task].items():
            if field not in ["task", "due_date", "priority_level"]:
                print(f"{field}: {value}")
                print("--------------------------")
                print("--------------------------")

        print("Do you want to add another task? (Y/N)")
        task_confirmation = input(">>> ").lower()

        if task_confirmation != "y":
            print("Exiting...")
            break


print("Hello. Welcome to To Do List..")
print("Add task only")
add_task()
