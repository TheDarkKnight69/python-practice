"""CONTACT BOOK"""
import json
import time

CONTACT_BOOK_PATH = "/workspaces/python-practice/programs/contact_book.json"

def to_camel_case(field):

    """ _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    """
    words = field.split(' ')
    return words[0] + ''.join(word.title() for word in words[1:])

def load_contact_book():
    """load_contact_book _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    """
    try:
        with open(CONTACT_BOOK_PATH, "r", encoding="utf-8") as file:  # noqa: E501
            contact_book = json.load(file)
            return contact_book

    except FileNotFoundError:
        # Return an empty dictionary if the file is not found
        return {}


CONTACT_BOOK = load_contact_book()

def add_contact():
    """Add a contact to the CONTACT_BOOK"""
    while True:
        print("Enter the name: ")
        name = input(">>> ")
        if name not in CONTACT_BOOK:
            print("Enter the age: ")
            age = int(input(">>> "))
            print("Enter the phone number: ")
            phone_number = int(input(">>> "))
            CONTACT_BOOK[name] = {
                "name": name,
                "age": age,
                "phone_number": phone_number
            }
            print("Do you want to add another field?:  (Y/N)")
            field_confirmation = input(">>> ").lower()
            while True:
                if field_confirmation != "y":
                    print("Okay. Proceeding")
                    break
                else:
                    print("Enter the field: ")
                    field = input(">>> ").lower()
                    print(f"Enter the value for the field '{field}': ")
                    field_value = input(">>> ")
                    CONTACT_BOOK[name][field] = field_value


        # Check if the contact name already exists
        else:
            # Contact already exists, update the additional field-value pair
            print("Contact already exists. Adding additional details.")
            print("Enter the field: ")
            field = input(">>> ").lower()
            print(f"Enter the value for the field '{field}': ")
            field_value = input(">>> ")
            CONTACT_BOOK[name][field] = field_value

        print("Okay! Added!")
        print("Contact Details:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Phone Number: {phone_number}")

        for field, value in CONTACT_BOOK[name].items():
            if field not in ['name', 'age', 'phone_number']:
                field_name = to_camel_case(field)
                print(f"{field_name}: {value}")
                break

       # Printing it because fancy
        print("Do you want to add another contact? (Y/N)")  # Asks for another contact
        confirmation = input(">>> ").lower()
        if confirmation != "y":  # if conf isn't "y" it breaks off.
            print("Okay! Proceeding. ")
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
        for field,value in contact.items():
            if field not in ['name', 'age','phone_number']:
                field_name = to_camel_case(field)
                print(f"{field_name}: {value}")
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
    """_summary_"""
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
    with open(CONTACT_BOOK_PATH, "w", encoding="utf-8") as file:  # noqa: E501
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
