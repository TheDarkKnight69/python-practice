import random

MAX_GUESSES = 5
guess_count = 0

conf = input("""
Welcome! Let's play Guess the Number! 
I will choose a random number between 0 and 100, 
and you will have to guess it. Based on your input, 
I will tell you if the entered number is higher or lower than mine! 
Got it? (Y/N): 
""")

if conf.lower() == "y" or conf.lower() == "yes":
  a = random.randint(0, 100)
  print("I have chosen my number! ")

  while guess_count < MAX_GUESSES:
    b = int(input("Enter your guess: "))
    guess_count += 1
    if b > a:
      print("Lower!")
    elif b < a:
      print("Higher!")
    else:
      print("Jackpot!")
      break

  if guess_count >= MAX_GUESSES:
    print(
      f"Sorry, you have reached the maximum number of {MAX_GUESSES} guesses. The number I was thinking of was {a}."
    )
else:
  print("That's alright! Take your time!")
