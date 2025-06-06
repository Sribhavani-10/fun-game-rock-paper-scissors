import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_result(player, computer):
    if player == computer:
        return "It's a draw!"
    elif (
        (player == 'rock' and computer == 'scissors') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'paper' and computer == 'rock')
    ):
        return "You win!"
    else:
        return "You lose!"