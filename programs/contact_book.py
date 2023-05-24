"""CONTACT BOOK"""
import json
import time


def load_contact_book():
    """
    Loads the contact book from a file
    """
    try:
        with open("contact_book.json", "r") as file:
            contact_book = json.load(file)
            return contact_book
    except FileNotFoundError:
        # Return an empty dictionary if the file is not found
        return {}

CONTACT_BOOK = load_contact_book()

def add_contact():
    """ We add a contact"""
    while True:
        # while loop for multiple times
        print("Enter the name: ")
        name = input(">>> ")
        print("Enter the age: ")
        age = input(">>> ")
        print("Enter the phone number: ")
        phone_number = int(input(">>> "))
        # Entering the details

        CONTACT_BOOK[name] = {
            'name': name,
            'age': age,
            'phone_number': phone_number
        }
        # Storing it in the dict
        print("Okay! Added!")
        print("Contact Details:")
        print(f'Name: {name}')
        print(f'Age: {age}')
        print(f'Phone Number: {phone_number}')
        # Printing it because fancy
        print("Do you want to add another contact? (Y/N)")  # Asks for another contact
        confirmation = input(">>> ").lower()
        if confirmation != "y":   # if conf isn't "y" it breaks off.
            print("Okay. Thank you!")
            break
def print_contact_book():
    """
    This prints the contact book
    """
    print("Contact Book:")
    for name, contact in CONTACT_BOOK.items():
        print("-------------------")
        print(f"Name: {contact['name']}")
        print(f"Age: {contact['age']}")
        print(f"Phone Number: {contact['phone_number']}")
        print("-------------------")




def delete_contact():
    """This deletes a contact from the contact book"""
    print("Okay. Enter the name of the contact you want to delete.")
    name = input(">>> ")
    print("Scanning the contact book...... ")
    time.sleep(2)
    if name in CONTACT_BOOK:
        del CONTACT_BOOK[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found. Are you sure that was the right name?")

def search_for_contact():
    """_summary_
    """
    print("Enter the name of the contact.")
    name = input(">>> ")
    print("Scanning the contact book..... Please wait")
    time.sleep(2)
    if name in CONTACT_BOOK.items():
        print("Found matches:")
        contact = CONTACT_BOOK[name]
        print(f"Contact details for {name}")
        print(f"Name: {contact['name']}")
        print(f"Age: {contact['age']}")
        print(f"Phone Number: {contact['phone_number']}")
    else:
        print("No matches found..... Please doublecheck the name.")

def save_contact_book():
    """save_contact_book _summary_

    _extended_summary_
    """
    with open('contact_book.json','w', encoding = 'utf-8') as file:
        json.dump(CONTACT_BOOK, file)

CONTACT_MESSAGE = """Welcome to the Contact Book!
Choose your action (1/2/3/4/5) from the below options:

1) Add a contact.
2) Delete a contact.
3) Search for a contact.
4) Display the contact book.


5) Exit


"""
print(CONTACT_MESSAGE)
while True:
    print("-------------------")
    choice = input(">>> ")
    print("-------------------")

    if choice == "1":
        add_contact()
        time.sleep(3)
        print(CONTACT_MESSAGE)
    elif choice == "2":
        delete_contact()
        time.sleep(5)
        print(CONTACT_MESSAGE)
    elif choice == "3":
        search_for_contact()
        time.sleep(5)
        print(CONTACT_MESSAGE)
    elif choice == "4":
        print_contact_book()
        time.sleep(5)
        print(CONTACT_MESSAGE)
    elif choice == "5":
        print("Thank you for using this program!")
        print("Saving the contact book now....")
        save_contact_book()
        break
    else:
        print("That was an invalid option.")
        print("Saving the contact book now....")
        print("Exiting program now....")
        break
        
