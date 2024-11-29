
# Game Theory: Rock-Paper-Scissors

## Problem
	Simulate a series of games of Rock-Paper-Scissors
	between two players, where each player randomly... or not...
    chooses their move.

## Challenge

- introduce biases
- introduce patterns
- introduce strategies

...and analyze how they affect the winning %

### 1st-rps-simulation-fair-game.py
Each player can choose from RPS, no bias, pure randomness.

### 2nd-rps-simulation-dumb-bias.py
Altering 1st - introducing a "dumb" bias - player 1 only chooses rock.

### 3rd-rps-simulation-bias-no-scissors.py
Altering 1st - another bias, player 1 does not use scissors at all.

### 4th-rps-simulation-bias-1.py
Altering 1st - Player 1 chooses 50% paper and the rest 25% each

### 4th-rps-simulation-bias-2.py
Altering 1st - bias in both players
- player 1 - 60% paper, rest 20% each
- player 2 - 60% scissors, rest 20% each

Numbers are really skewed here:

    Player 1 wins:  194823  ~ 38.96 %
    Player 2 wins:  305177  ~ 61.04 %


### 5st-rps-simulation-pattern.py
Altering 1st - Player 1 chooses by iterator value (iteration_start).

### 6th-rps-simulation-strategy-if-loose-play-winner-if-win-keep.py
Altering 1st - player 1 will keep the selection if it wins and use 
the winner selection in the next round if looses.

### 7th-rps-simulation-strategy-if-win-play-opp-else-play-not-played.py
Altering 1st - player 1 will play the opponent choice if he wins, 
else he will play something that wasn't played in the prev. round.  

### 7th-rps-simulation-strategy-if-win-play-opp-else-play-not-played-with-bias.py
Altering 7th -  keep the prev. algorithm for the 1st player,
    bias for the 2nd one:
- ~57,14% for paper
- ~28,57% for scissors
- ~14,28% for rock

Given the above the skewness is minimal:

    Player 1 wins:  259588  ~ 51.92 %
    Player 2 wins:  240412  ~ 48.08 %



----------
Inspiration: https://medium.com/ground-state-curiosity/how-to-probably-win-at-rock-paper-scissors-172aa3e768a8

