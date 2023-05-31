"""Rock-Paper-Scissors Game"""
import random

print("""Hello! 
Welcome to the Rock Paper Scissors game in python. I hope you know this works.
For people who don't: 
You will enter your choice from "rock/paper/scissors" and I will play my choice.
The hierarchy is as follows:
1) Rock beats Scissors
2) Scissors beat Paper
3) Paper beats Rock
4) All like items cancel each other out!

Got it?
Press Enter if you are ready to play!
""")
bot_choices = ["rock", "paper", "scissors"]
conf = input()
if conf == "":
  print("Alright! On your call!")
  print("Enter your choice! Remember the hierarchy is above! ")
  while True:
    choice = input(">>> ").lower()

    my_choice = random.choice(bot_choices)

    loss = "I lost! Good Job!"
    win = f"I win! {my_choice.capitalize()} beats {choice.capitalize()}! GG!"
    tie = "That was a tie! Your go again!"
    if choice == "rock" and my_choice == "scissors":
      print(loss)
      break
    elif choice == "rock" and my_choice == "paper":
      print(win)
      break
    elif choice == "rock" and my_choice == "rock":
      print(tie)

    elif choice == "paper" and my_choice == "scissors":
      print(win)
      break
    elif choice == "paper" and my_choice == "rock":
      print(loss)
      break
    elif choice == "paper" and my_choice == "paper":
      print(tie)

    elif choice == "scissors" and my_choice == "rock":
      print(win)
      break
    elif choice == "scissors" and my_choice == "paper":
      print(loss)
      break
    elif choice == "scissors" and my_choice == "scissors":
      print(tie)

    else:
      print("That was an invalid input. Please try again: ")
      choice = input(">>> ")
