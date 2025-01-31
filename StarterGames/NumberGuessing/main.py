from art import logo
import random

def guess_the_number():
    guess_function = True
    while guess_function:
        print(logo)
        print("Welcome to the Number Guessing Game!")
        numbers = []
        for num in range(0, 100):
            numbers.append(num)
        print("I'm thinking of a number between 1 and 100.")
        answer = random.choice(numbers)
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == 'easy':
            lives = 10
            print(f"You have {lives} attempts remaining to guess the number.")
        elif difficulty == 'hard':
            lives = 5
            print(f"You have {lives} attempts remaining to guess the number.")
        else:
            print("You did not provide a valid input.")
            break
        game = True
        while game:
            print(answer)
            guess = int(input("Make a guess: "))
            if guess != answer:
                lives -= 1
                if lives > 0:
                    print(f"You have {lives} attempts remaining to guess the number.")
                    if guess > answer:
                        print("Too high! Guess again.")
                    elif guess < answer:
                        print("Too low! Guess again.")
                    if guess not in numbers:
                        print("Your guess was not within the range. Please try again.")
                else:
                    print(f"You've run out of guesses, the answer is {answer}. You lose!\n")
                    play_again = input("Would you like to play again? Type 'y' or 'n': ")
                    if play_again == 'y':
                        print(logo)
                        print("Welcome to the Number Guessing Game!")
                        print("I'm thinking of a number between 1 and 100.")
                        answer = random.choice(numbers)
                        if difficulty == 'easy':
                            lives = 10
                        elif difficulty == 'hard':
                            lives = 5
                        else:
                            print("You did not provide a valid input.")
                            break
                        guess_function = True
                    elif play_again == 'n':
                        print("Thanks for playing! Have a good day!")
                        guess_function = False
                        break
                    else:
                        print("You did not provide a valid input.")
                        guess_function = False
                        break

            else:
                print(f"You got it! The answer is {answer}.")
                play_again = input("Would you like to play again? Type 'y' or 'n': ")
                if play_again == 'y':
                    print(logo)
                    print("Welcome to the Number Guessing Game!")
                    print("I'm thinking of a number between 1 and 100.")
                    answer = random.choice(numbers)
                    if difficulty == 'easy':
                        lives = 10
                    elif difficulty == 'hard':
                        lives = 5
                    else:
                        print("You did not provide a valid input.")
                        break
                    guess_function = True
                elif play_again == 'n':
                    print("Thanks for playing! Have a good day!")
                    guess_function = False
                else:
                    print("You did not provide a valid input.")
                    guess_function = False
def ask():
    play_or_not = input("Would you like to play a number guessing game? (y/n): ")
    if play_or_not.lower() == 'y':
        guess_the_number()
    elif play_or_not.lower() == 'n':
        print("No problem with that, have a good day!")
    else:
        print("You did not provide a valid input. Try again.\n")
        ask()
ask()