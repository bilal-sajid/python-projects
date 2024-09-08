from game_data import data
import random
import art

def select_random_choice():
    return random.choice(data)

def compare_guess(user_selection, other_selection):
    if user_selection >= other_selection:
        return True
    else:
        return False

print(art.logo)

# Selecting a Random Option (A)
option_A = select_random_choice()
# print("Option A: ",option_A)

game_running = True
score = 0

while game_running:

    # Selecting a Random Option (B)
    option_B = select_random_choice()
    # print("Option B: ",option_B)

    print()
    print(f"Compare A: {option_A['name']}, a {option_A['description']}, from {option_A['country']}")
    # print(option_A['follower_count']) # To Check

    print("vs")

    print(f"Against B: {option_B['name']}, a {option_B['description']}, from {option_B['country']}")
    # print(option_B['follower_count']) # To Check

    # Compare the guesses
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    correct = False

    if guess == 'A':
        correct = compare_guess(option_A['follower_count'], option_B['follower_count'])
    elif guess == 'B':
        correct = compare_guess(option_B['follower_count'], option_A['follower_count'])
    else:
        print("Invalid input")
        correct = None

    print()

    if not correct:
        print("Sorry that's wrong")
        print("Your final score is:", score)
        game_running = False
        print("\n" * 5)
    elif correct:
        score += 1
        print("You're Correct! Your current score is", score)

        # If the correct option is B then give option B to option A
        if guess == 'B':
            option_A = option_B

        print("\n" * 5)
