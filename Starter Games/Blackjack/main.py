from art import logo
import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")

if play == 'y':
    def blackjack():
        print(logo)
        card_reset = True
        while card_reset:
            card1 = random.choice(cards)
            card2 = random.choice(cards)
            score = card1 + card2
            player_cards = [card1, card2]
            comp_first_card = random.choice(cards)
            comp_cards = [comp_first_card]
            comp_score = comp_first_card

            game = True
            while game:
                print(f"Your cards: {player_cards}, current score: {score}")
                print(f"Computer's first card: {comp_first_card}")

                hit_or_stand = input("Type 'y' to get another card or type 'n' to pass: ")
                if hit_or_stand == 'y':
                    hit = random.choice(cards)
                    player_cards.append(hit)
                    score += hit
                    if score > 21:
                        print(f"Your final hand: {player_cards}, final score: {score}")
                        print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
                        print("You went over. You lose!\n")
                        play_again = input("Do you want to play again? Type 'y' or 'n': ")
                        if play_again == 'y':
                            print(logo)
                            card_reset = True
                        else:
                            print("Good game, thanks for playing!")

                if hit_or_stand == 'n':
                    comp_cards.append(random.choice(cards))
                    comp_score = sum(comp_cards)
                    while comp_score < score:
                        new_card = random.choice(cards)
                        comp_cards.append(new_card)
                        comp_score += new_card
                    print(f"Your final hand: {player_cards}, final score: {score}")
                    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
                    if score > 21:
                        print("You went over. You lose!\n")
                        play_again = input("Do you want to play again? Type 'y' or 'n': ")
                        if play_again == 'y':
                            print(logo)
                            card_reset = True
                        else:
                            print("Good game, thanks for playing!")
                    else:
                        if comp_score > 21:
                            print("Opponent went over. You win!\n")
                            play_again = input("Do you want to play again? Type 'y' or 'n': ")
                            if play_again == 'y':
                                print(logo)
                                card_reset = True
                            else:
                                card_reset = False
                                print("Good game, thanks for playing!")
                        elif score > comp_score:
                            print(f"You win!\n")
                            play_again = input("Do you want to play again? Type 'y' or 'n': ")
                            if play_again == 'y':
                                print(logo)
                                card_reset = True
                            else:
                                card_reset = False
                                print("Good game, thanks for playing!")
                        elif score == comp_score:
                            print("Draw.\n")
                            play_again = input("Do you want to play again? Type 'y' or 'n': ")
                            if play_again == 'y':
                                print(logo)
                                card_reset = True
                            else:
                                card_reset = False
                                print("Good game, thanks for playing!")
                        else:
                            print("You lose!\n")
                            play_again = input("Do you want to play again? Type 'y' or 'n': ")
                            if play_again == 'y':
                                print(logo)
                                card_reset = True
                            else:
                                card_reset = False
                                print("Good game, thanks for playing!")
    blackjack()
else:
    print("Okay, have a good day!")