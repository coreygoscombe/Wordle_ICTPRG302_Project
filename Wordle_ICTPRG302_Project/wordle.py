# ASSESSMENT_TITLE
#
# Author: Corey Goscombe
# Student ID: 20155074
#
# Course: ICTPRG302
# Lecturer: Para O'Kelly

# heads up! this program requires all_words.txt and target_words.txt

# Imports
import random
from time import sleep
from string import ascii_letters
from os import system
# Variables and Constants
DEBUG = False
name = ''
scene = 0 # this decides what scene will be showing (e.g. gameplay, winning, losing)
# 0 = Welcome, 1 = Instructions, 2 = Gameplay, 3 = Lose Screen, 4 = Win Screen
valid_words = []
possible_target_words = []
def init():
    global allowed_guesses
    global target_word
    global split_target
    global score
    global previous_guesses
    global yellow_list
    global greens
    global previous_scores
    allowed_guesses = 6
    target_word = ""
    split_target = []
    score = 0
    previous_guesses = []
    previous_scores = []
    yellow_list = []
    greens = ''


# Application Functions

def score_guess(guess):
    '''
    Analyses the guess, adds score, and checks if the game should end.

    Arguments
    ---------
    - guess - the word guessed, to be scored

    Returns
    ---------
    - adds score according to guess
    - a change in scene if required
    - puts all correct letters in the right list
    - puits all yellow letters to the yellow list

    Examples
    --------
    target word = "GREEN"
    score_guess("BLUES")
    output adds 2 to the score and continues the game

    target word = "GREEN"
    score_guess("GREEN")
    output will end the game
    '''
    global previous_guesses
    global previous_scores
    global allowed_guesses
    global target_word
    global scene
    global score
    allowed_guesses -= 1
    split_guess = list(guess)
    for letter in range(0,5):
        if split_guess[letter] == split_target[letter]:
            score += 2
            previous_scores.append("O")
        elif split_guess[letter] in target_word:
            score += 1
            previous_scores.append("?")
        else:
            previous_scores.append("-")
    previous_guesses.append(''.join(split_guess))
    if allowed_guesses <= 0:
        scene = 3
    elif guess_word == target_word:
        scene = 4

def read_words(txt):
    words = []
    file = open(txt,"r")
    for line in file:
        words.append(line.rstrip())
    file.close()
    return words


def show_greeting():
    global name
    name = input("Please enter your name: ")
    print(f"Welcome To Pydle, {name}!")

def show_instructions(show_modes):
    global target_word
    global split_target
    print("Instructions")
    print("You will have 6 guesses to guess a 5 letter word.")
    print("When you guess, you'll see a row above your word.")
    print("That's the stats about the word.")
    print("O = Correct, ? = Not the right spot, - = Does not appear")
    print("Good luck!")
    print("Upon typing 'help' these instructions will appear")
    print("for 10 seconds.")
    if show_modes == True:
        print("Select a mode:")
        print("Normal: The regular Pydle Experience")
        print("Crazy: Any and all words allowed!")

def show_win():
    global target_word
    global score
    system("cls || clear")
    print("Congratulations! you win!")
    print("The word was: " + target_word)
    print(f"Score: {score}")
    sleep(4)

def show_lose():
    global target_word
    global score
    system("cls || clear")
    print("You lose! :(")
    print("The word was: " + target_word)
    print(f"Score: {score}")
    sleep(4)
     
def valid_word_check(guess):
    global valid_words
    for word in valid_words:
        if guess.lower() == word:
            return True
    return False

def random_word():
    return random.choice(possible_target_words).upper()

def display_score():
    global previous_guesses
    global previous_scores
    print("Previous guesses: ")
    increment = 0
    for guess in range(len(previous_guesses)):
        print(previous_guesses[guess])
        print(''.join(previous_scores[increment:increment+5]))
        increment += 5

def play_game():
    system("cls || clear")
    global previous_guesses
    global guess_word
    global allowed_guesses
    global target_word
    global greens
    global score
    global name
    print(name)
    display_score()
    print(f"Guesses Left: {allowed_guesses}")
    print(f"Current word: {greens}")
    print(f"Score: {score}")
    guess_word = input("Your Guess?: ")
    if guess_word.lower() == 'help':
        system("cls || clear")
        show_instructions(False)
        sleep(10)
    else:
        str(guess_word)
        guess_word = guess_word.upper()
        if mode == "normal":
            if valid_word_check(guess_word) == True:
                score_guess(guess_word)
        else:
            if len(guess_word) == 5:
                score_guess(guess_word)

def test_game():
    global target_word
    target_word = "HORSE"
    play_game()

init()
valid_words = read_words("all_words.txt")
possible_target_words = read_words("target_words.txt")
while True:
    if scene == 0:
        show_greeting()
        scene = 1
    elif scene == 1:
        show_instructions(True)
        mode = input("Your selection: ")
        try:
            if mode.lower() == "normal":
                target_word = random_word()
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
        scene = 1
        system("cls || clear")
        init()
    elif scene == 4:
        show_win()
        scene = 1
        system("cls || clear")
        init()
