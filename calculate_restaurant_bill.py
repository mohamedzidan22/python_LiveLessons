# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 01:54:45 2024

@author: MOHAMED

assume that the tax on a restaurant bill is 6.25% and that the bill amount is
37.45. usr the type Decimal to calculate the bill total then print the result with
two digits to the right of the decimal point

"""

from decimal import Decimal

tax = Decimal('.0625')

bill_amount = Decimal('37.45')

total_bill = (tax + 1) * bill_amount

print(f'The total bill after tax is: {total_bill:.2f}')