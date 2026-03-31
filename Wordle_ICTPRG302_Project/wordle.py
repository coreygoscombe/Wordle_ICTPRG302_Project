# ASSESSMENT_TITLE
#
# Author: Corey Goscombe
# Student ID: 20155074
#
# Course: ICTPRG302
# Lecturer: Para O'Kelly

# Imports
import random
# Variables and Constants
DEBUG = False
valid_words = []
possible_target_words = []
allowed_guesses = 6
target_word = ""
split_target = []
score = 0
scene = 1 # this decides what scene will be showing (e.g. gameplay, winning, losing)
# 1 = gameplay, 2 = lose screen, 3 = win screen
previous_guesses = []
guess_greens = ["-","-","-","-","-"]
guess_yellows = [] 


# Application Functions
# TODO: Score Guess Function
def readwords():
    global valid_words
    global possible_target_words
    file = open("all_words.txt","r")
    for line in file:
        valid_words.append(line.rstrip())
    file.close()
    file = open("target_words.txt","r")
    for line in file:
        possible_target_words.append(line)
    file.close()
# TODO: Display Greeting Function
def show_greeting():
    print("Welcome")

# TODO: Display Instructions Function
def show_instructions():
    print("Instructions")

# TODO: Any Optional Additional Functions 

# TODO: Play Game Function
def play_game():
    print("\033c", end="")
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
    eval_word()

def eval_word():
    global guess_word
    global previous_guesses
    global allowed_guesses
    str(guess_word)
    guess_word = guess_word.upper()
    if valid_word_check() == True:
        allowed_guesses -= 1
        split_guess = list(guess_word)
        for letter in range(0,5):
            if split_guess[letter] == split_target[letter]:
                guess_greens[letter] = split_target[letter]
            elif split_guess[letter] in target_word:
                if split_guess[letter] not in guess_yellows:
                    guess_yellows.append(split_guess[letter])
        previous_guesses.append(''.join(split_guess))

def valid_word_check():
    global valid_words
    global guess_word
    for word in valid_words:
        if guess_word.lower() == word:
            return True
    return False


#TODO: Testing Function
def test_game():
    target_word = "GREEN"
#TODO: Main Program
readwords()
target_word = random.choice(possible_target_words).upper()
split_target = list(target_word)
while True:
    if DEBUG == True:
        test_game()
    else:
        play_game()
