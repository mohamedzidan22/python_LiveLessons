# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:09:14 2024

@author: MOHAMED

flipping a coin 20 times

"""

#import the random module
import random
#initialize 2 variables to store heads and tails frequencies
heads_frequency = 0
tails_frequency = 0

#flip the coin 20 times
for flipping in range(20):
    result = random.randrange(1,3)
    if result == 1:
        heads_frequency += 1
    if result == 2:
        tails_frequency += 1

#display the result
print(f'{"face"}{"frequency":>13}')
print(f'{"H":>3}{heads_frequency:>13}')
print(f'{"T":>3}{tails_frequency:>13}')
