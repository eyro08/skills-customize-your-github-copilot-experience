
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a playable Hangman game in Python to practice string manipulation, loops, conditionals, random selection, and user input.

## 📝 Tasks

### 🛠️ Set Up the Hidden Word

#### Description

Create the game data and select a hidden word for the player to guess.

#### Requirements

Completed program should:

- Store multiple possible words in a predefined list.
- Randomly select one word from the list at the start of each game.
- Create a masked display with one underscore for each letter in the hidden word.

### 🛠️ Implement the Guessing Game

#### Description

Create a game loop that accepts letter guesses, updates the masked word, and ends with the appropriate result.

#### Requirements

Completed program should:

- Accept a letter guess from the player and show the current progress, such as `_ _ _`.
- Track and display the number of incorrect guesses remaining.
- Reveal every matching occurrence when the guessed letter appears more than once.
- End when the player guesses the whole word or runs out of attempts.
- Display a clear win or lose message when the game ends.

Example progress:

```text
Hidden word: python
Guess a letter: p
Progress: p _ _ _ _ _
```
