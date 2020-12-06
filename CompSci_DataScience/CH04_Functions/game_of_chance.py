"""Simulating the dice game Craps"""
import random

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    return (dice1, dice2)   # pack dice face values into a tuple

def display_dice(dice):
    """Display one roll of the two dice."""
    dice1, dice2 = dice     # unpack the tuple nito variables dice1 and dice2
    print(f'Player rolled {dice1} + {dice2} = {sum(dice)}')

dice_values = roll_dice()   # first roll
display_dice(dice_values)

# determine game status and point, based on first roll
sum_of_dice = sum(dice_values)

if sum_of_dice in (7, 11):  # win
    game_status = 'WON'
elif sum_of_dice in (2, 3, 12): # lose
    game_status = 'LOST'
else:   # remember point
    game_status = 'CONTINUE'
    my_point = sum_of_dice
    print('Point is', my_point)

# continue rolling until player wins or loses
while game_status == 'CONTINUE':
    dice_values = roll_dice()
    display_dice(dice_values)
    sum_of_dice = sum(dice_values)

    if sum_of_dice == my_point:     # win by making point
        game_status = 'WON'
    elif sum_of_dice == 7:          # lose by rolling 7
        game_status = 'LOST'

# display "wins" or "loses" message
if game_status == 'WON':
    print('Player wins')
else:
    print('Player loses')