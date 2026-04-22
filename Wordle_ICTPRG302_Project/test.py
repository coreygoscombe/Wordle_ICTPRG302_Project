valid_words = []
possible_target_words = []
def read_words(txt):
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
target_word = "GLUES"
split_target = list(target_word)
def score_guess(guess):
    '''
    Scores the guess based on how many yellows/greens there are.

    Arguments
    ---------
    - guess - the word guessed, to be scored

    Returns
    ---------
    - it returns a list of each letter's score.

    Examples
    --------
    target word = "GREEN"
    score_guess("BLUES")
    output = [0,0,0,2,0]

    target word = "GREEN"
    score_guess("GREEN")
    output = [2,2,2,2,2]
    '''
    global target_word
    score = []
    split_guess = list(guess)
    for letter in range(0,5):
        if split_guess[letter] == split_target[letter]:
            score.append(2)
        elif split_guess[letter] in target_word:
            score.append(1)
        else:
            score.append(0)
    if guess == target_word:
        score = [2,2,2,2,2]
    return score
read_words()
guess_word = input("Enter guess:").upper()
if guess_word in valid_words:
    print(score_guess())