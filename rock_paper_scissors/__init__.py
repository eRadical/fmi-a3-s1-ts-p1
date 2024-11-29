
import random
# import numpy as np

iterations = 500_000

DEBUG = False

CHOICE_ROCK = "rock"
CHOICE_PAPER = "paper"
CHOICE_SCISSORS = "scissors"

def random_extract_from_choices(given_choices):
    """Extract a random choice from the given choices."""
    return random.choice(given_choices)

def get_winner(choice_player1, choice_player2):

    if DEBUG: print(choice_player1, choice_player2)

    if choice_player1 == choice_player2:
        return 0

    if choice_player1 == CHOICE_ROCK:
        if choice_player2 == CHOICE_SCISSORS:
            if DEBUG:
                print("Rock smashes scissors! Player1 wins!")
            return 1
        else:
            if DEBUG:
                print("Paper covers rock! Player1 loses.")
            return 2
    elif choice_player1 == CHOICE_PAPER:
        if choice_player2 == CHOICE_ROCK:
            if DEBUG:
                print("Paper covers rock! Player1 wins!")
            return 1
        else:
            if DEBUG:
                print("Scissors cuts paper! Player2 wins!")
            return 2
    elif choice_player1 == CHOICE_SCISSORS:
        if choice_player2 == CHOICE_PAPER:
            if DEBUG:
                print("Scissors cuts paper! Player1 wins!")
            return 1
        else:
            if DEBUG:
                print("Paper covers scissors! Player2 loses.")
            return 2

def print_results(nr_of_ties, player1_wins, player2_wins, player1_plays_by_choice, player2_plays_by_choice, player1_wins_by_choice, player2_wins_by_choice):
    print("Ties: ", nr_of_ties)
    print("Player 1 wins: ", player1_wins, " ~", round(player1_wins * 100 / iterations, 2), "%")
    print("Player 2 wins: ", player2_wins, " ~", round(player2_wins * 100 / iterations, 2), "%")
    print("------------------------------------------------------------------------------------------------------")
    print("Player 1 non-tie plays: ", player1_plays_by_choice)
    print("Player 2 non-tie plays: ", player2_plays_by_choice)
    print("------------------------------------------------------------------------------------------------------")

    print("Player 1 wins\n=================")
    print("{:<10} {:<10} {:<5}".format('Key', 'Number', 'Perc %'))
    for k, v in player1_wins_by_choice.items():
        print("{:<10} {:<10} {:<5}".format(k, v, round(v * 100 / player1_wins, 2)))
    print("------------------------------------------------------------------------------------------------------")

    print("Player 2 wins\n=================")
    print("{:<10} {:<10} {:<5}".format('Key', 'Number', 'Perc %'))
    for k, v in player2_wins_by_choice.items():
        print("{:<10} {:<10} {:<5}".format(k, v, round(v * 100 / player2_wins, 2)))
