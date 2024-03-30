# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 19:08:24 2024

@author: MOHAMED

what happens when we randomly roll a die 1000 times?
what are the probabilities of each face of this die?

P(face_num) = (1/6) * number of rolls

"""
#import the random module to mkae use of its functions
import random

#initialize six variables. each variable will contain the number of times each face will appear
frequency_1 = 0
frequency_2 = 0
frequency_3 = 0
frequency_4 = 0
frequency_5 = 0
frequency_6 = 0

#roll the die a thousand times

for roll in range(1000):
    result = random.randrange(1, 7)
    #check the result and increment its frequency by 1
    if result == 1:
        frequency_1 += 1
    if result == 2:
        frequency_2 += 1
    if result == 3:
        frequency_3 += 1
    if result == 4:
        frequency_4 += 1
    if result == 5:
        frequency_5 += 1
    if result == 6:
        frequency_6 += 1

#Display the result in columnar format

print(f'{"face"}{"frequency":>13}')
print(f'{1:>4}{frequency_1:>13}')
print(f'{2:>4}{frequency_2:>13}')
print(f'{3:>4}{frequency_3:>13}')
print(f'{4:>4}{frequency_4:>13}')
print(f'{5:>4}{frequency_5:>13}')
print(f'{6:>4}{frequency_6:>13}')














