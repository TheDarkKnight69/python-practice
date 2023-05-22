import pyAesCrypt
import string
import random
import os
import getpass
import time

password = ""  # Global variable to store the password


def encrypt_file():
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
        "File/Path is valid.                        Encryption process.....[1/2]"
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

  global password
  password = ""
  if password_choice == "1":
    password = getpass.getpass("Enter your password to encrypt: ")

  elif password_choice == "2":
    password = "".join(
      random.choices(string.ascii_letters + string.digits, k=5))
    print("Generated password:", password)
  time.sleep(1)
  print("Password OK!                         Encryption process.....[2/2]")

  try:
    print("File Encrypting.......")
    time.sleep(1)
    pyAesCrypt.encryptFile(input_file, output_file, password)

    print("File encrypted successfully!")
  except Exception as e:
    print("Encryption failed:", str(e))


def decrypt_file():
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
        "File/Path is valid.                       Decryption process.....[1/2]"
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
  if entered_password == password:
    print("Password Match!               Decryption Process.....[2/2]")
    time.sleep(1)
    try:
      print("File Decrypting.......")
      time.sleep(1)
      pyAesCrypt.decryptFile(encrypted_file, decrypted_file, entered_password)
      os.remove(encrypted_file)
      print("File decrypted successfully!")
    except Exception as e:
      print("Decryption failed:", str(e))
  else:
    time.sleep(1)
    print("Password is not a match!                    Decryption Failed")


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
