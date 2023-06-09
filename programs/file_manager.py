"""File Manager Program.
Uses os library to make, delete and edit files."""

import os
import time
from colorama import Style, Fore

def print_tree(path, level=0, prefix='', padding=''):
    """Prints the File Directory"""
    if level == 0:
        print(padding[:-1] + '+--' + os.path.basename(path) + '/')
    items = os.listdir(path)
    for i, item in enumerate(sorted(items)):
        full_path = os.path.join(path, item)
        is_last = i == len(items) - 1
        if os.path.isdir(full_path):
            print(prefix + '+-- ' + item)
            sub_prefix = prefix + '|     ' if not is_last else prefix + '        '
            print_tree(full_path, level + 1, sub_prefix)
        else:
            print(prefix + '|-- ' + item)


print("""
Welcome to a file utility in Python!
Please choose from the following options:
1) Create/Make a file with some content inside.
2) Rewrite the file.
3) Add some content in an existing file.
4) Delete a file.
5) Display the contents of the file.
6) Display the list of files.

7) Exit!

P.S Your choice should look something like: 1 or 2
""")
while True:
    DIRECTORY = "file_directory"
    if not os.path.exists(DIRECTORY):
        # create the directory
        os.makedirs(DIRECTORY)
        print(f"The directory '{DIRECTORY}' has been created.")
    a = input(Fore.YELLOW + ">>> " + Style.RESET_ALL)
    if a == "1":
        print("Okay, please specify the file name: ")
        filename = input(Fore.YELLOW + ">>> " + Style.RESET_ALL) + ".txt"
        with open(os.path.join(DIRECTORY, filename), 'w', encoding="utf-8") as f:
            print("Now, input the content of the file: ")
            content = input(Fore.YELLOW + ">>> " + Style.RESET_ALL)
            f.write(content)
            print("Content Written.")
            print("Your choice: ")
    elif a == "2":
        print("Okay, tell me the name of the file: ")
        filename = input(Fore.YELLOW + ">>> " + Style.RESET_ALL) + ".txt"
        if os.path.exists(os.path.join(DIRECTORY, filename)):
            # remove the file if it already exists
            os.remove(os.path.join(DIRECTORY, filename))
            with open(os.path.join(DIRECTORY, filename), 'w', encoding="utf-8") as f:
                print("Now, input the content of the file: ")
                content = input(Fore.YELLOW + ">>> " + Style.RESET_ALL)
                f.write(content)
                print("Content Rewritten.")
                print("Your choice: ")

    elif a == "3":
        print("Okay, please specify the file name: ")
        filename = input(">>> ") + ".txt"
        if os.path.exists(os.path.join(DIRECTORY, filename)):
            with open(os.path.join(DIRECTORY, filename), 'a', encoding="utf-8") as f:
                print("Input the content of the file: ")
                content = input(">>> ")
                f.write(" " + content)
                print("Content written.")
                print("Your choice: ")
    elif a == "4":
        print("Okay, tell me the name of the file: ")
        filename = input(">>> ") + ".txt"
        if os.path.exists(os.path.join(DIRECTORY, filename)):
            # remove the file if it already exists
            os.remove(os.path.join(DIRECTORY, filename))
            print("File Deleted!")
            print("Your choice: ")
    elif a == "5":
        print("Okay, please specify the file name: ")
        filename = input(">>> ") + ".txt"
        if os.path.exists(os.path.join(DIRECTORY, filename)):
            with open(os.path.join(DIRECTORY, filename), 'r', encoding="utf-8") as f:
                print(f.read())

    elif a == "6":
        print("Please hang on..")
        time.sleep(3)
        print_tree(DIRECTORY)
        print("Your choice: ")
    elif a == "7":
        print("Thank you for using this program!")
        break
    else:
        print("Invalid input!")
        print("Try again: ")
