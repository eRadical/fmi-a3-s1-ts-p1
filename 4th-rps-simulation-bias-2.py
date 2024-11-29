
import rock_paper_scissors
from rock_paper_scissors import CHOICE_ROCK, CHOICE_SCISSORS, CHOICE_PAPER

choices_player1 = [CHOICE_ROCK, CHOICE_SCISSORS, CHOICE_PAPER, CHOICE_PAPER, CHOICE_PAPER]
choices_player2 = [CHOICE_ROCK, CHOICE_SCISSORS, CHOICE_SCISSORS, CHOICE_SCISSORS, CHOICE_PAPER]

################################ Things to analyze

### How many times each player won?
player1_wins = 0
player2_wins = 0
nr_of_ties = 0

### Distribution of plays by choice per player
player1_plays_by_choice = { CHOICE_ROCK: 0, CHOICE_SCISSORS: 0, CHOICE_PAPER: 0 }
player2_plays_by_choice = { CHOICE_ROCK: 0, CHOICE_SCISSORS: 0, CHOICE_PAPER: 0 }

### Distribution of wins by choice per player
player1_wins_by_choice = { CHOICE_ROCK: 0, CHOICE_SCISSORS: 0, CHOICE_PAPER: 0 }
player2_wins_by_choice = { CHOICE_ROCK: 0, CHOICE_SCISSORS: 0, CHOICE_PAPER: 0 }

# Code
iteration_start = 0
while iteration_start < rock_paper_scissors.iterations:
    p1 = rock_paper_scissors.random_extract_from_choices(choices_player1)
    p2 = rock_paper_scissors.random_extract_from_choices(choices_player2)

    winner = rock_paper_scissors.get_winner(p1, p2)
    if winner == 0:     ### eliminate non-combat, we're interested only in winning situations
        nr_of_ties += 1
    else:
        iteration_start += 1
        ### Plays by choice but only when we have a winner
        player1_plays_by_choice[p1] += 1
        player2_plays_by_choice[p2] += 1

    if winner == 1:
        player1_wins += 1
        player1_wins_by_choice[p1] += 1

    if winner == 2:
        player2_wins += 1
        player2_wins_by_choice[p2] += 1

### Print results
rock_paper_scissors.print_results(nr_of_ties,
    player1_wins, player2_wins,
    player1_plays_by_choice, player2_plays_by_choice,
    player1_wins_by_choice, player2_wins_by_choice
)
