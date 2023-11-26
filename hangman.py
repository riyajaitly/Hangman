'''
assignment: PA1: Hangman

author: Riya Jaitly

date: October 6, 2022

file: hangman.py is a program that replicated the game of hangman for the 
user to play. 

input: the program asks the user to enter in the word length o#f the 
word they would like to to guess and the amount of lives they want. The lives 
represent the amount of tries they have for a wrong input. The user is then 
asked to input a guess of a letter that may be in the word. After the user 
either guesses the word or runs out of lives, the user will be asked whether 
they would like to play again and will input their answer as Y/y (yes) or N/n (no).


output: The game in the program is the output.
'''

from curses.ascii import isdigit
from random import choice, sample, randint, randrange

dictionary_file = "dictionary.txt"
#dictionary_file = "dictionary-short.txt"
#dictionary_file = "/Users/riyajaitly/CSE 30/Hangman/dictionary.txt"

print("Welcome to the Hangman Game!")

guessed_lists = []
out = ""

#dictionary textfile words added to dictionary in program
def import_dictionary (filename):
    count = 0
    file1 = open(filename, 'r')
    dictionary = {}
    while True:
        count += 1
    
        line = file1.readline()
        line = line.replace(" ", "")
        line = line.replace("\n", "")

        if not line:
            return dictionary
        else:
            dictionary[count] = line
    file1.close()
    
    return dictionary

#Create "O" for how mnay lives user inputs and changes to "X" when they lose life
def num_lives(p_initial_lives, p_word_lives):
    l_lives = ""
    nx = p_initial_lives - p_word_lives
    for i in range(p_initial_lives):
        if i < nx:
            l_lives = l_lives + "X"
        else:
            l_lives = l_lives + "O"
    return l_lives

#generates random word for hangman game from dictionary
def get_random_word(p_dictionary, p_word_len):
    l = len(p_dictionary)
    rand_num = randint(1,l)
    d = p_dictionary[rand_num]
    r_word_len = len(d)

    while r_word_len != p_word_len:
        rand_num = randint(1,l)
        d = p_dictionary[rand_num]
        r_word_len = len(d)

    return(d)

#asks user to input word length and number of lives they want
def get_game_options():
    word_len = input("Please choose a size of a word to be guessed [3 - 12, default any size]: \n")
    if word_len.isdigit():
        word_len = int(word_len)
        if 3 <= word_len <= 12:
            print("The word size is set to " + str(word_len) + ".")
        else:
            print("A dictionary word of any size will be chosen.")    
            word_len = randint(3,12)
    else:
        print("A dictionary word of any size will be chosen.")    
        word_len = randint(3,12)

    word_lives = input("Please choose a number of lives [1 - 10, default 5]: \n")

    if word_lives.isdigit():
        word_lives = int(word_lives)
        if 1 <= word_lives <= 10:
            print("You have " + str(word_lives) + " lives.")
        else:
            print("You have 5 lives.")
            word_lives = int(5)
    else:
        print("You have 5 lives.")
        word_lives = int(5)

    print("Letters chosen: " )

    size = word_len
    lives = word_lives

    return(size, lives)

dictionary_2 = {}
dictionary_2 = import_dictionary(dictionary_file)


play_again = 'Y'

#repeats code if user enter "Y: or "y" when asked to play again
while play_again == 'Y':
    guessed_lists = [] #empty list when playing again
    t = get_game_options()
    
    word_len = t[0]
    word_lives = t[1]
    initial_lives = word_lives
    word = get_random_word(dictionary_2, word_len).upper()
    
    #print(word) #[answer printed!!!!!!!]


    
    #################

    print_out = 1
    
    while word_lives > 0:

        out = ""
        out_space = ""
        for letter in word:
            if letter in guessed_lists:
                out = out + letter
                out_space = out_space + letter + " "
            else:
                if letter == "-":
                    out = out + "- " 
                    out_space = out_space + "- "
                else:
                    out = out + "__ " 
                    out_space = out_space + "__ "
        
        if out == word:
            break
        
        if print_out == 1:
            print(out_space + " lives: " + str(word_lives) + " " + num_lives(initial_lives, word_lives))
        
         
        print("Please choose a new letter >")

        guess = input()

        while len(guess) == 0:
            print("Please choose a new letter >")
            guess = input()
        
        
        guess  = guess.upper()


        if guess in guessed_lists:
            print("You have already chosen this letter.")
            print_out = 0

        elif guess in word:
            guessed_lists.append(guess)
            print("You guessed right!")
            print("Letters chosen:", end=' ')
            print(*guessed_lists, sep =', ')
            print_out = 1

        else:
            guessed_lists.append(guess)
            print("You guessed wrong, you lost one life.")
            print("Letters chosen:", end=' ')
            print(*guessed_lists, sep =', ')
            word_lives = word_lives - 1
            print_out = 1



    if word_lives:
        print(out_space + " lives: " + str(word_lives) + " " + num_lives(initial_lives, word_lives))
        print("Congratulations!!! You won! The word is " + word.upper() + "!")
    else:
        print(out_space + " lives: " + str(word_lives) + " " + num_lives(initial_lives, word_lives))
        print("You lost! The word is " + word.upper() + "!")

    play_again = input(str("Would you like to play again [Y/N]?\n"))
    if play_again == "Y" or play_again == "y":
        play_again = 'Y'
    else:
        print("Goodbye!")
        play_again = 'N'