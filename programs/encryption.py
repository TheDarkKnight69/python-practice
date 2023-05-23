"""
Encryption/Decription Program
"""


import os
import string
import random
import getpass
import time
import pyAesCrypt

PASSWORD = None

def encrypt_file():
    """
    Encrypts a file using pyAesCrypt. 
    Takes a password and uses it or generates a random 5-character password"""
    global PASSWORD
    print("Enter the name of the file that you want to encrypt:")
    file_name = input(">>> ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    while True:
        if os.path.exists(file_name):
            input_file = file_name
            time.sleep(1)
            output_file = file_name[:-4] + "_encrypted.txt"
            print(
                "File/Path is valid.                                Encryption process.....[1/2]"
            )
            break
        else:
            print(
                "File/Path not found. Please ensure that you have typed in the correct path."
            )
            print("Enter the name of the file that you want to encrypt:")
            file_name = input(">>> ")
            if not file_name.endswith(".txt"):
                file_name += ".txt"

    print("Enter the password for encryption:")
    print("Press 1 for a custom password")
    print("Press 2 for a randomly generated 5-character password")
    password_choice = input(">>> ")
    if password_choice == "1":
        PASSWORD = getpass.getpass("Enter your password to encrypt: ")

    elif password_choice == "2":
        PASSWORD = "".join(
            random.choices(string.ascii_letters + string.digits, k=5))
        print("Generated password:", PASSWORD)
    time.sleep(1)
    print("Password OK!                                       Encryption process.....[2/2]")
    error_message = ""
    try:
        print("File Encrypting.......")
        time.sleep(1)
        pyAesCrypt.encryptFile(input_file, output_file, PASSWORD)

        print("File encrypted successfully!")
    except FileNotFoundError as error_message:
        print("File not found:", str(error_message))
    except ValueError as error_message:
        print("Value error:", str(error_message))
    except PermissionError as error_message:
        print("Permission error:", str(error_message))
    except FileExistsError as error_message:
        print("File exists error:", str(error_message))



def decrypt_file():
    """
    Decrypts a file using pyAesCrypt. 
    Takes the set password and uses it to decrypt"""
    print("Enter the name of the file that you want to encrypt:")
    print("Enter the name of the file that you want to decrypt:")
    encrypted_file = input(">>> ")
    time.sleep(1)

    while True:
        if not encrypted_file.endswith(".txt"):
            encrypted_file += ".txt"
        if os.path.exists(encrypted_file):
            decrypted_file = encrypted_file[:-14] + "_decrypted.txt"
            time.sleep(1)
            print(
                "File/Path is valid.                                   Decryption process.....[1/2]"
            )
            break
        else:
            time.sleep(1)
            print(
                "File/Path not found. Please ensure that you have typed in the correct path."
            )
            print("Enter the name of the file that you want to decrypt:")
            encrypted_file = input(">>> ")
            if not encrypted_file.endswith(".txt"):
                encrypted_file += ".txt"
                decrypted_file = encrypted_file[:-14] + "_decrypted.txt"

    entered_password = getpass.getpass("Please enter your password: ")
    if entered_password == PASSWORD:
        print("Password Match!                             Decryption Process.....[2/2]")
        time.sleep(1)
        error_message = ""
        try:
            print("File Decrypting.......")
            time.sleep(1)
            pyAesCrypt.decryptFile(encrypted_file, decrypted_file, entered_password)
            os.remove(encrypted_file)
            print("File decrypted successfully!")
        except FileNotFoundError as error_message:
            print("File not found:", str(error_message))
        except ValueError as error_message:
            print("Value error:", str(error_message))
        except PermissionError as error_message:
            print("Permission error:", str(error_message))
        except FileExistsError as error_message:
            print("File exists error:", str(error_message))
        else:
            time.sleep(1)
            print("Password is not a match!                     Decryption Failed")


print("Welcome to an Encryption/Decryption Program!!")
print("Press 1 for encrypting a file.")
print("Press 2 for decrypting a file.")
while True:
    choice = input(">>> ").lower()

    if choice == "1":
        encrypt_file()
        print("Press 1 for encrypting a file.")
        print("Press 2 for decrypting a file.")

    elif choice == "2":
        decrypt_file()
        print("Press 1 for encrypting a file.")
        print("Press 2 for decrypting a file.")
    elif choice == "exit" or choice == "quit":
        print("Thank you for using this program! ")
        break
    else:
        print("Invalid choice!")
        break
