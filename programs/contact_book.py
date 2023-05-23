#CONTACT BOOK 
import time

CONTACT_BOOK = {}

def add_contact(): 
    # We add a contact
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
    # This prints the contact book
    print("Contact Book:")
    for name, contact in CONTACT_BOOK.items():   # We reiterate over these in the dict
        print(f"Contact Details for {name}:")
        print(f"Name: {contact['name']}")
        print(f"Age: {contact['age']}")
        print(f"Phone Number: {contact['phone_number']}")
        print("-------------------")
        print("-------------------")


def delete_contact():
    #This deletes a contact from the contact book
    print("Okay. Enter the name of the contact you want to delete.")
    name = input(">>> ")
    print("Scanning the contact book...... ")
    time.sleep(2)
    if name in CONTACT_BOOK['name']:
      del CONTACT_BOOK['name']
      print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found. Are you sure that was the right name?")


def search_for_contact():
    FloatingPointError
        

CONTACT_MESSAGE = """Welcome to the Contact Book!
Choose your action (1/2/3/4/5) from the below options:

1) Add a contact. 
2) Delete a contact. *
3) Search for a contact. *
4) Display the contact book. *


5) Exit.


[* Not Implemented]
"""  
print(CONTACT_MESSAGE)
while True:
    print("-------------------")
    choice = input(">>> ")
    print("-------------------")

    if choice == "1":
        add_contact()
        print(CONTACT_MESSAGE)
    elif choice == "2":
        delete_contact()
        print(CONTACT_MESSAGE)
    elif choice == "4":
        print_contact_book()
        print(CONTACT_MESSAGE)
