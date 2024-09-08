import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy or 'hard: ")
    
    if level == "easy":
        return EASY_LEVEL_ATTEMPTS

    
    elif level == "hard":
        return HARD_LEVEL_ATTEMPTS
    
    else:
        print("Invalid Input. You gave 10 guesses.")
        return EASY_LEVEL_ATTEMPTS


def compare_guess(user_guess, actual_answer, left_attempts):
    """
    Checks the guess againt the answer
    Returns number of attempts left
    """
    if user_guess > actual_answer:
        print("\nToo high. Guess again")
        return (left_attempts - 1)

    elif user_guess < actual_answer:
        print("\nToo low. Guess again")
        return (left_attempts - 1)

    else:
        print(f"\nYou got it! The answer was {actual_answer}")



def game():

    print("\nWelcome to the Number Guesser Game")
    print("\nI'm thinking of a number between 1 and 100.")
    selected_number = random.randint(0,100)

    attempts = set_difficulty()
    guess = -10

    while guess != selected_number:
        print(f"\nYou have {attempts} attempts available to guess the number")
        guess = int(input("Make a guess: "))
        
        attempts = compare_guess(guess, selected_number, attempts)
        
        if attempts == 0:
            print("You've run out of guesses. You Lose")
            return

game()