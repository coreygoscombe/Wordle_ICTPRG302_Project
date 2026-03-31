# ASSESSMENT_TITLE
#
# Author: Corey Goscombe
# Student ID: 20155074
#
# Course: ICTPRG302
# Lecturer: Para O'Kelly

# Imports
import random
from time import sleep
from string import ascii_letters
from clear import clear # requires installation from pip :)
# Variables and Constants
DEBUG = False
valid_words = []
possible_target_words = []
allowed_guesses = 6
target_word = ""
split_target = []
score = 0
scene = 0 # this decides what scene will be showing (e.g. gameplay, winning, losing)
# 0 = Welcome, 1 = Instructions, 2 = Gameplay, 3 = Lose Screen, 4 = Win Screen
previous_guesses = []
guess_greens = ["-","-","-","-","-"]
guess_yellows = [] 


# Application Functions

def eval_word():
    global guess_word
    global previous_guesses
    global allowed_guesses
    allowed_guesses -= 1
    split_guess = list(guess_word)
    for letter in range(0,5):
        if split_guess[letter] == split_target[letter]:
            guess_greens[letter] = split_target[letter]
        elif split_guess[letter] in target_word:
            if split_guess[letter] not in guess_yellows:
                guess_yellows.append(split_guess[letter])
    previous_guesses.append(''.join(split_guess))

def readwords():
    global valid_words
    global possible_target_words
    file = open("all_words.txt","r")
    for line in file:
        valid_words.append(line.rstrip())
    file.close()
    file = open("target_words.txt","r")
    for line in file:
        possible_target_words.append(line.rstrip())
    file.close()


def show_greeting():
    print("Welcome To Pydle!")
    sleep(2)

def show_instructions():
    global target_word
    global split_target
    print("Instructions")
    print("You will have 6 guesses to guess a 5 letter word")
    print("Any letter that fits in the right place")
    print("will display at the bottom.")
    print("'Yellow' letters are letters that appear")
    print("in the correct word at any point")
    print("at any amount.")
    print("Good luck!")
    print("")
    print("Select a mode:")
    print("Normal: The regular Pydle Experience")
    print("Crazy: Any and all words allowed!")
            
def valid_word_check():
    global valid_words
    global guess_word
    for word in valid_words:
        if guess_word.lower() == word:
            return True
    return False

def play_game():
    clear()
    yellows = ''.join(guess_yellows)
    greens = ''.join(guess_greens)
    global previous_guesses
    global guess_word
    global allowed_guesses
    print("Previous guesses: ")
    for guess in previous_guesses:
        print(guess)
    print(f"Guesses Left: {allowed_guesses}")
    print(f"Current word: {greens}")
    print(f'Yellow: {yellows}')
    guess_word = input("Your Guess?: ")
    str(guess_word)
    guess_word = guess_word.upper()
    if mode == "normal":
        if valid_word_check() == True:
            eval_word()
    else:
        if len(guess_word) == 5:
            eval_word()

def test_game():
    target_word = "GREEN"
    DEBUG = False

readwords()
while True:
    if scene == 0:
        show_greeting()
        scene = 1
    elif scene == 1:
        show_instructions()
        mode = input("Your selection: ")
        try:
            if mode.lower() == "normal":
                target_word = random.choice(possible_target_words).upper()
                split_target = list(target_word)
                scene = 2
            elif mode.lower() == "crazy":
                target_letters = []
                while len(target_letters) < 5:
                    target_letters.append(random.choice(ascii_letters))
                target_word = ''.join(target_letters)
                target_word = target_word.upper()
                split_target = list(target_word)
                scene = 2
        except ValueError:
            print("Incorrect syntax!")
    elif scene == 2:
        if DEBUG == True:
            test_game()
        else:
            play_game()
    elif scene == 3:
        show_lose()
    elif scene == 4:
        show_win()
