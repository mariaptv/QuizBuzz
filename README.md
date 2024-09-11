# Quiz Game

A simple command-line quiz game that asks the user a series of True/False questions. The game ends if the user gets a question wrong or all questions are answered.

## Features

- A list of questions is displayed one at a time.
- The user inputs `True` or `False` to answer.
- The game continues until either the user answers all questions correctly or gets one wrong.

## How It Works

1. The `QuizBrain` class manages the logic of the game, including the question flow and checking if there are any remaining questions.
2. The `Question` class models each question with its `text` and `answer`.
3. The game reads a list of questions from the `question_data` and builds a quiz.

## Code Structure

- `QuizBrain`: Handles the game logic (e.g., checking if there are more questions, presenting the next question, and verifying the answers).
- `Question`: Represents individual quiz questions.
- The game loop runs until there are no more questions or the user gets a question wrong.

## Project Structure

