import random
import string

print("Hello! Welcome to Password Generator!")
length = int(input("Enter the length of the password you wish to be: \n>>> "))

password = "".join(
  random.choices(string.ascii_letters + string.digits, k=length))
print(f"The password generated is : {password}")
print("Do you want another go? (Y/N)")
conf = input().lower()

while True:
  if conf == "y":
    password = "".join(
      random.choices(string.ascii_letters + string.digits, k=length))
    print(f"The password generated is : {password}")
    print("Do you want another go? (Y/N)")
    conf = input().lower()
  else:
    print("Thank you!")
    break
