"""
Hangman Game With Gallows
"""


import requests
from nltk.corpus import wordnet as wn


def get_word_subject(word):
    """
    Hint for word
    """
    # Get synset for word
    synsets = wn.synsets(word)

    # Extract hypernym (generalization) for synset
    if synsets:
        synset = synsets[0]    # Use first synset as default
        hypernym = synset.hypernyms()[0].name()
        return hypernym.split('.')[0]
    else:
        return "Unknown"


def draw_gallows(guesses_remaining):
    """
    Gallows
    """
    print("""
     _____
    |         |
    |         {}
    |        {}{}{}
    |        {} {}
    |
-----------
Guesses remaining: {}
""".format("O" if guesses_remaining < 6 else "",
                     "/" if guesses_remaining < 5 else " ",
                     "|" if guesses_remaining < 4 else "",
                     "\\" if guesses_remaining < 3 else "",
                     "/" if guesses_remaining < 2 else "",
                     "\\" if guesses_remaining < 1 else "", guesses_remaining))


word_url = "https://random-word-api.herokuapp.com/word?length=5"
word = requests.get(word_url)
data1 = word.json()
data = data1[0]

guess = 0
max_guesses = 6
print("""
Let's play Hangman!
""")
print("I have thought of a word!! Your turn to guess.")
print(f"The subject is {get_word_subject(data)}")
a = list(data)
i = "_" * len(a)
while guess < max_guesses:
    g = input("Guess: (This should generally be only one letter) ")
    if g in a or g == a:
        print("Correct!")
        for j in range(len(a)):
            if a[j] == g or a == g:
                i = i[:j] + g + i[j + 1:]
    else:
        print("Incorrect!")
        guess += 1
    print("Current word: ", i)
    draw_gallows(max_guesses - guess)
    if i == data:
        print("Congratulations! You have won!")
        break
    elif guess == max_guesses:
        print("Sorry, you have run out of guesses. The word was:", data)
        break
