# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)

lives_easy = 10
lives_hard = 5

secret_number = random.randint(1, 100)


def choose_difficulty(difficulty):
    if difficulty == "easy":
        return lives_easy
    if difficulty == "hard":
        return lives_hard
    else:
        difficulty = input("Invalid input. Type 'easy' or 'hard': ")
        return choose_difficulty(difficulty)


def compare(guess, remaining_attempts):
    if guess != secret_number:
        remaining_attempts -= 1
        print(
            f"You have {remaining_attempts} attempts remaining to guess the number."
        )
        if guess > secret_number:
            print("Too high.")
        if guess < secret_number:
            print("Too low.")
        print("Guess Again")
    if guess == secret_number:
        print(f"You got it! The answer is {guess}")
    return remaining_attempts


print("Welcome to the Number Guessing Game!")
# print(f"Psst the correct answer is {secret_number}")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
remaining_attempts = choose_difficulty(difficulty)
print(f"You have {remaining_attempts} attempts remaining to guess the number.")

game_over = False
while not game_over:
    guess = int(input("Make a guess: "))
    remaining_attempts = compare(guess, remaining_attempts)
    if guess == secret_number:
        game_over = True
    if remaining_attempts == 0:
        print("You've run out of guesses, You lose!")
        game_over = True
