# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 01:32:26 2024

@author: MOHAMED

if we have a deposite with 1000$ with a yearly interst of 5% we wnat to know
how much money will be in the account at the end of each year

the realtion is total = p(1+ interst)**2

NOTICE: we are about to make monetary calculation so we need to use the object
time Decimal from the class decimal

"""
from decimal import Decimal

principle = Decimal('1000.00')
interst = Decimal(.05)

for year in range(1, 11):
    total = principle*(1 + interst)**year
    print(f'{year:>2} {total:>10.2f}')
