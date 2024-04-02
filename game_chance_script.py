"""
31-Mar-2024	7:48 PM

A practical a example on randomness

the game is simple: you roll two dice, if your result is 7 or 11, you win.
if your result is 2, 3 or 12, you lose.
if your result is 4, 5, 6, 8, 9 or 10, you have another 7 attempts to try to repeat you result, otherwise you lose.

HINT: it turns out that i misunderstood the original game example from the Live Lessons, which produced a whole different game. However my game still valid logical-wise and syntax-wise. The original game will be implmented in a separate script

"""
#import randomness to our world
import random


#roll the 2 dice
for roll in range(1):
	die1 = random.randrange(1, 7)
	for roll in range(1):
		die2 = random.randrange(1, 7)
print("First die is: ", die1)
print("Second die is: ", die2)
point = die1 + die2


#check the result
if point == 7 or point == 11:
	print(f'{"You Won! "}{"Your result is: "}{point}')
elif point == 2 or point == 3 or point == 12:
	print(f'{"You Lost! "}{"Your result is: "}{point}')



#the 7 attempts phase
else:
	print("Your point is: ", point)
	counter = 7
	for roll in range(7):
		die1_2 = random.randrange(1, 7)
		counter -= 1
		for roll in range(8):
			die2_2 = random.randrange(1, 7)
		point2 = die1_2 + die2_2
		print("Your attempt is", point2)
		if point2 == point:
			print(f'{"You win! "}{"You repeated your point: "}{point2}')
			break
		else:
			print("You didn't make your point, You still have", counter, "attmpts")

