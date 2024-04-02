"""
The game is simple: you rol1 the dice, if it sums 7 or 11, then you win
if it sums 2, 3 or 12 you lose
if it 4, 5, 6, 8, 9, 10, then this is your point
you roll the dice again until you get your point
if you get 7, you lose
---------------------------------------------------------------------
PSEUDOCODE

ROLL THE DICE
	roll the dice
	return the two results in a tuple
DISPLAY THE SUM OF DICE RESULT
	unpack the tuple to a variable
	print the sum of the unpacked tuple
IF DICE IS IN 7, 11. WIN
	check the sum_of_dice is in 7 or 11
	set game_status to WON
IF DICE IS IN 2, 3, 12. LOSE
	check the sum_of_dice is in 2, 3 or 12
	set game_status to LOSE
IF DICE IS IN 4, 5, 6, 8, 9, 10. CONTINUE
	check sum_of_dice
	make sum_of_dice = my_point
	set game_status to CONTINUE
	
ROLL THE DICE AGAIN if game_status = CONTINUE
	IF DICE = FIRST ROLL DICE. WIN
	IF DICE = 7. LOSE

DISPLAY THE GAME RESULT
"""
import random

def roll_dice():
	die1 = random.randrange(1, 7)
	die2 = random.randrange(1, 7)
	return (die1, die2)


def display_result(dice):
	die1, die2 = dice
	print(f'Player rolled {die1} + {die2} = {sum(dice)}')


dice_result = roll_dice()
display_result(dice_result)

sum_of_dice = sum(dice_result)


if sum_of_dice in (7, 11):
	game_status = 'WON'

elif sum_of_dice in (2, 3, 12):
	game_status = 'LOSE'
	
else:
	game_status = 'CONTINUE'
	my_point = sum_of_dice
	print("point is:", my_point)

while game_status == 'CONTINUE':
	dice_result = roll_dice()
	display_result(dice_result)
	sum_of_dice = sum(dice_result)

	if sum_of_dice == my_point:
		game_status = 'WON'
		
	elif sum_of_dice == 7:
		game_status = 'LOSE'
		

if game_status == 'WON':
	print("PLAYER WINS!")
else:
	print("PLAYER LOSES!")