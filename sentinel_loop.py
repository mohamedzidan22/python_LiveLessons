# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:52:11 2024

@author: MOHAMED
"""

""" Sentinel iteration used when i don't know how many times i want to iterate"""

#intialization phase
total = 0
grade_counter = 0

#process phase
grade = int(input('enter your grade, -2 to terminate: '))
while grade != -2:
    total = grade + total
    grade_counter += 1
    grade = int(input('enter your grade, -2 to terminate: '))

#termination phase
if grade_counter != 0:
    print(f'the avg grade is = {total / grade_counter:.2f}')
else:
    print('No grades have been entered')