# Hangman Game

Welcome to the Hangman Game, a variation of the classic Hangman game. In this game, you'll be tasked with guessing a hidden word letter by letter. Be careful, as incorrect guesses will lead to the display of a hangman figure, and you'll need to guess the word before the figure is completed!

## How to Play

1. Run the `hangman.py` script to start the game.
2. The computer will choose a random word, and the word's length will be represented by dashes, with revealed vowels.
3. Guess a letter or the entire word. If the guessed letter is correct, it will be revealed in its correct position(s) in the word.
4. Each incorrect guess will increment the hangman figure's progress, displayed after every guess.
5. If you guess the entire word correctly, you win! If the hangman figure is completed before you guess the word, you lose.

## Files

- `hangman.py`: The main Hangman game script.
- `words.py`: Contains a list of words that the Hangman game selects from.
- `logo.py`: Contains a list of ASCII art hangman logos for each stage of the game.

## Rules

- The computer will reveal vowels in the chosen word, but consonants will appear as dashes.
- Guessing a letter correctly will reveal its positions in the word.
- Guessing a word correctly will instantly win the game.
- An incorrect guess will progress the hangman figure, displayed after every guess.
- Guessing a wrong word will progress the hangman figure by two steps.
- The player wins if they guess the word before the hangman figure is fully displayed.