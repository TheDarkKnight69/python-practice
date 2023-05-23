# Welcome to my Python Program Dump!
# There are 6 different programs that I have created. You are free to use any of them for yourself.


# [Encryption Program](https://github.com/TheDarkKnight69/python-practice/blob/f17ff986f55150eaa2059882194a951273213521/programs/encryption.py)
    
This program is an Encryption/Decryption utility that allows you to encrypt and decrypt files using the pyAesCrypt library in Python.

When you run the program, you will be presented with a menu of options:

1) Encrypt a file: This option allows you to encrypt a file. You will be prompted to enter the name of the file you want to encrypt. If the file exists, you will be prompted to choose a password. You can either enter a custom password or generate a random 5-character password. The file will be encrypted using the chosen password and saved as "filename_encrypted.txt".

2) Decrypt a file: This option allows you to decrypt a previously encrypted file. You will be prompted to enter the name of the encrypted file you want to decrypt. If the file exists, you will be prompted to enter the password used for encryption. If the entered password matches the one used for encryption, the file will be decrypted and saved as "filename_decrypted.txt".

The program handles various error scenarios such as file not found, incorrect passwords, and permission errors. It uses the `pyAesCrypt` library for encryption and decryption.

Please note that the program uses a global variable `PASSWORD` to store the password. The password is set during the encryption process and must match the entered password during decryption.

You can choose the encryption or decryption option by entering "1" or "2" respectively. To exit the program, you can enter "exit" or "quit".

Enjoy encrypting and decrypting files using this program!
  
  Screenshots:
  
  
   ![image](https://github.com/TheDarkKnight69/python-practice/assets/91176991/8cd273e8-1cd3-4f1c-958c-982f9e99fcc8)



# [File Manager](https://github.com/TheDarkKnight69/python-practice/blob/f17ff986f55150eaa2059882194a951273213521/programs/file_manager.py)
  This program is a file manager utility that allows you to perform various operations on files using the `os` library in Python.

When you run the program, you will be presented with a menu of options to choose from:

1) Create/Make a file with some content inside.
2) Rewrite the file.
3) Add some content in an existing file.
4) Delete a file.
5) Display the contents of the file.
6) Display the list of files.
7) Exit the program.

To select an option, enter the corresponding number. For example, if you want to create a file, enter "1". The program will guide you through the specific actions based on your choice.

Here's a brief explanation of each option:
1) Create/Make a file: You can specify a file name and enter the content for the file. The file will be created in a directory called "file_directory".
2) Rewrite the file: You can choose an existing file, provide new content, and overwrite the existing content of the file.
3) Add some content: You can choose an existing file and add new content to it without overwriting the existing content.
4) Delete a file: You can choose an existing file and delete it.
5) Display file contents: You can choose an existing file and view its contents.
6) Display the list of files: It will display the file directory tree structure, showing all the files and subdirectories within the "file_directory".
7) Exit the program: This option allows you to exit the program.

The program provides prompts for input and displays relevant messages based on the actions performed.

Please note that the file directory "file_directory" will be automatically created if it doesn't exist.

Enjoy managing and manipulating files using this program!
 
 Screenshots:
  
  
   ![image](https://github.com/TheDarkKnight69/python-practice/assets/91176991/9c744693-00ea-4b54-9865-0a45fcac68f0)
   
  
# [Guess The Number](https://github.com/TheDarkKnight69/python-practice/blob/f17ff986f55150eaa2059882194a951273213521/programs/file_manager.py)
This program is a "Guess the Number" game. The program will choose a random number between 0 and 100, and you need to guess the number. 
It will provide hints to let you know if your guess is higher or lower than the chosen number.

The game starts by displaying a welcome message and asking if you're ready to play. If you respond with "yes" or "y," the program will generate a random number and let you know it has chosen a number.

You have a maximum number of guesses defined as 5. You will be prompted to enter your guess, and the program will compare it with the chosen number. If your guess is higher than the chosen number, it will tell you to guess lower. If your guess is lower, it will tell you to guess higher. If you guess the correct number, it will display "Jackpot!" and you win the game.

If you reach the maximum number of guesses without guessing the correct number, it will display a message stating that you have reached the maximum number of guesses and reveal the chosen number.

If you decide not to play by responding with "no" or any other response, it will display a message to take your time.

Enjoy playing the game and see if you can guess the number correctly within the given number of guesses!



Screenshots:


   ![image](https://github.com/TheDarkKnight69/python-practice/assets/91176991/4c2fc7c7-e608-41e7-a687-696d833f4938)



# [Hangman](https://github.com/TheDarkKnight69/python-practice/blob/f17ff986f55150eaa2059882194a951273213521/programs/hangman.py)
This code is a Hangman game in Python. 
In this game, the program selects a random word and you need to guess it by entering one letter at a time. 
The program will provide hints for the word's subject to help you guess.

The game starts by displaying the gallows and the number of guesses remaining. 
You need to guess the word by entering a letter. 
If your guess is correct, the program will show you the current state of the word with the correctly guessed letters filled in. 
If your guess is incorrect, the program will increment the guess count and draw more of the gallows. 

You win the game by correctly guessing all the letters of the word before running out of guesses. 
If you guess all the letters, the program will display a congratulatory message. 
If you run out of guesses before guessing the word, it will reveal the word and inform you that you've lost.

It's an enjoyable game to test your word-guessing skills and have fun with friends. Give it a try and see how many words you can guess correctly!




Screenshots:

   ![image](https://github.com/TheDarkKnight69/python-practice/assets/91176991/51646431-624f-419e-ab1e-89bf8d2912da)




# [Password Generator](https://github.com/TheDarkKnight69/python-practice/blob/f17ff986f55150eaa2059882194a951273213521/programs/password_generator.py)

This code is a password generator program. 
It asks you how long you want the password to be and then creates a random password for you. 
The password will have a mix of letters (both uppercase and lowercase) and numbers. 
It shows you the password it created, and if you want, you can generate another password. 
It's a simple and handy tool to create strong passwords easily. Give it a try and keep your accounts secure! lol




Screenshots:


    
   ![image](https://github.com/TheDarkKnight69/python-practice/assets/91176991/d3cbbdba-6e38-481d-8376-5c44278abd76)
   
   
   
   
# [Rock - Paper - Scissors](https://github.com/TheDarkKnight69/python-practice/blob/f17ff986f55150eaa2059882194a951273213521/programs/RPS.py)

This code is a Rock-Paper-Scissors game in Python. 
It's a two-player game where you play against the computer. 
You choose either "rock," "paper," or "scissors," and the computer will also make its choice. 
The game follows a hierarchy: rock beats scissors, scissors beat paper, and paper beats rock. If both players choose the same item, it's a tie.

To play, you need to enter your choice, and the program will compare it with the computer's choice. 
It will then determine the winner based on the hierarchy. 
If you win, it will display a message saying you won and how you beat the computer. If you lose, it will show that you lost. 
If it's a tie, it will let you play again.

It's a fun and simple game to play when you're bored or want to challenge the computer. Give it a try and see if you can beat the computer!




Screenshots:


  
  
  ![image](https://github.com/TheDarkKnight69/python-practice/assets/91176991/0d54aa3d-4716-4379-9841-ef69a5474596)
  ![image](https://github.com/TheDarkKnight69/python-practice/assets/91176991/aa1be970-a920-4cfa-ba77-c66931185c29)
  ![image](https://github.com/TheDarkKnight69/python-practice/assets/91176991/e89c40b2-49a6-428e-a21e-0b9349d1ad48)

























#
#### PS: the descriptions were made by ChatGPT

