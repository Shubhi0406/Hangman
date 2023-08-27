import random
import logo
from words import words


def play_game():
    """Starts a game of Hangman"""
    is_game_over = False
    cur_step = 1
    # This will be the string printed to user, which includes some revealed letters and dashes
    cur_guessed = ""
    # Print the figure corresponding to the stage of the game
    print(logo.logos[cur_step-1])
    # For each letter in the word, it checks if its a vowel, and if it is, reveals that letter to the user.
    # Otherwise, displays a dash.
    for char in word:
        if char in "aeiou":
            cur_guessed += char
        else:
            cur_guessed += "_"
    print(cur_guessed)
    while not is_game_over:
        # During each turn, it asks the user to input a letter/word and passes the letter to the check() function
        letter = input("Guess a letter/word: ").lower()
        cur_guessed, cur_step = check(letter, cur_guessed, cur_step)
        # Prints figure for current stage and prints the string with some revealed letters and some dashes
        print(logo.logos[cur_step - 1])
        print(cur_guessed)
        # If the string returned from the check() function is the actual word (i.e. without any dashes), the user wins
        if cur_guessed == word:
            print("Congratulations! You have guessed the word.")
            print(f"The word was {word}")
            is_game_over = True
        # If the user has reached the last stage but has not guessed the word, they lose
        elif cur_step >= 7:
            print(f"You lost. The word was {word}")
            is_game_over = True


def check(letter, cur_guessed, cur_step):
    """Checks the validity of the guessed letter and checks if it belongs in the word"""
    # The cur_guessed string will be updated in this new string
    new = ""
    # Checks if the user has already guessed the letter/word and doesn't deduct a turn in that case
    if letter in guessed:
        print("You have already guessed this letter/word")
    # If the letter guessed is a vowel, it doesn't deduct a turn and instead asks for a consonant
    # (since it had revealed all vowels at the start of the game)
    elif letter in "aeiou":
        print("The letter you guessed is a vowel. You have to guess a consonant")
    # Checks if the guessed word is the chosen word
    elif letter == word:
        print("Correct!")
        new = word
    # Checks if letter is in the chosen word
    elif letter in word:
        print("Correct!")
        # Adds the already revealed letters and the guessed letter to the new string in the correct positions
        # Adds dashes if the letter has not been guessed yet
        for char in word:
            if char == letter or char in cur_guessed:
                new += char
            else:
                new += "_"
        # Adds the letter to the list of already guessed letters
        guessed.append(letter)
    # If the letter is wrong, moves to next stage of the game and the letter is added to the guessed list
    # Also checks if they guessed a word instead of a letter, and increases the stage of the game by 2 turns
    else:
        print("Wrong")
        guessed.append(letter)
        if len(letter) > 1:
            cur_step += 2
        else:
            cur_step += 1
    # If new is still an empty string, that means that no more letters are revealed and new and cur_guessed will be
    # the same
    if not new:
        new = cur_guessed
    # Returns the new string and the current stage to the play_game() function to update the variable there
    return new, cur_step


print("""
GAME RULES:
This is a variation of the classic Hangman game
. The computer will choose a random word and display dashes based on the word's length. But it will reveal the letters that are vowels.
. The user will guess a letter and if it is in the word, the computer will display the previously printed word with the new letter in the correct positions.
. During any turn, the user may guess a word instead of a single letter if they feel sure of it. But if the word is wrong, they will lose 2 turns.
. The user will win if they can guess the word before the figure shows the whole man being hanged. The figure will be printed after every guess.
""")
while input("\nDo you want to play a game of Hangman? Type 'y' or 'n': ") == "y":
    # Chooses a random word from the list of words given in words.py
    word = random.choice(words).lower()
    # This will contain the letters that the user has guessed. Will become an empty list whenever a new game begins.
    guessed = []
    play_game()
