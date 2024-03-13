# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:04:49 2024

@author: MOHAMED
"""

# Detecting the minimum number out of a a given list of numbers

#accept the first number
number_1 = int(input("Enter first number: "))
#accept the second number
number_2 = int(input("Enter second number: "))
#accept the third number
number_3 = int(input("Enter third number: "))
#accept the minimum value
minimum = number_1
#if S_num < minimum
if number_2 < minimum:
    minimum = number_2
#if TH_num < minimum
if number_3 < minimum:
    minimum = number_3
#print the output
print('The minimum number is ', minimum)
