# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:26:44 2024

@author: MOHAMED
"""

#create variables total, countr
total = 0
countr = 0
#declare the list of grades
grades = [65, 78, 66, 87, 44, 76, 12, 99]
#iterate using the counter
for grade in grades:
    #add tot the total while iterating
    total += grade
    #add one to the countr
    countr += 1
#use the expression total/countr to calculate the avg of the grades
AVG_grade = total / countr
#print the avg to the screen
print("The average of the grades is: ", AVG_grade)