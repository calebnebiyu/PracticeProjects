from art import logo
from game_data import data
from art import vs
import random


def higher_or_lower():
    print(logo)
    current_score = 0
    a_celebrity = random.choice(data)
    game = True
    while game:
        print(f"Compare A: {a_celebrity["name"]}, a {a_celebrity["description"]}, from {a_celebrity["country"]}.")
        print(vs)
        b_celebrity = random.choice(data)
        while a_celebrity == b_celebrity:
            b_celebrity = random.choice(data)
        print(f"Against B: {b_celebrity["name"]}, a {b_celebrity["description"]}, from {b_celebrity["country"]}.")
        choice = input("Who has more followers? Type 'A' or 'B': ")

        if choice == 'A' and a_celebrity["follower_count"] > b_celebrity["follower_count"]:
            current_score += 1
            print("\n" * 20)
            print(f"You're right! Current Score: {current_score}")
            a_celebrity = b_celebrity
        elif choice == 'B' and b_celebrity["follower_count"] > a_celebrity["follower_count"]:
            current_score += 1
            print("\n" * 20)
            print(f"You're right! Current Score: {current_score}")
            a_celebrity = b_celebrity
        else:
            final_score = current_score
            print("\n" * 20)
            print(f"Sorry, you're wrong. Game Over!\nFinal Score: {final_score}")
            game = False

play = input("Do you want to play Higher or Lower? Type 'Y' or 'N': ")
if play == 'Y' or play == 'y':
    higher_or_lower()
    play_again = input("Do you want to play again? Type 'Y' or 'N': ")
    if play_again == 'Y' or play_again == 'y':
        higher_or_lower()
    elif play_again == 'N' or play_again == 'n':
        print("Thanks for playing!")
else:
    print("Ok, have a good day!")