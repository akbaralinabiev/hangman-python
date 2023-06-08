# Hangman Game

This is a simple Hangman game implemented in Python. The game randomly selects a word from a list of words and the player has to guess the letters in the word within a limited number of attempts.

## Prerequisites

- Python 3.x

## How to Run

1. Clone the repository or download the `main.py` file.

2. Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

3. Run the following command to start the game:

   ```shell
   python main.py

4. The game will prompt you to enter letters as your guesses. Enter a single letter and press Enter to submit your guess.

5. Continue guessing letters until you either guess the word correctly or run out of lives

## Customizing the Word List

The game uses a predefined word list from the words module. If you want to customize the word list, you can modify the words list in the words.py file. Add or remove words as desired.

## Gameplay
* The game starts with a randomly selected word from the word list.

* The word is displayed as a series of dashes, with each dash representing a letter in the word.

* Guess letters by entering them one at a time. The game will inform you whether the letter is in the word or not.

* If your guess is correct, the corresponding dashes will be replaced with the correct letter in the word.

* If your guess is incorrect, you will lose a life. The number of remaining lives will be displayed.

* You can see the letters you have already guessed and the number of lives remaining at each turn.

* Keep guessing letters until you either guess the word correctly or run out of lives.

## Game Outcome

If you guess the word correctly before running out of lives, you win the game.

---

Feel free to customize and modify the code according to your needs. Enjoy playing Hangman!
