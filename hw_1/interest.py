"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""


interest = float(input('Enter the fixed interest rate in percent: '))
invest = float(input('Enter the amount of money you want to invest: '))
years = int(input('Enter the number of years the money will be invested: '))


calc1 = invest * (1 + (interest / 100)) ** years 


calc2 = calc1 - invest


print(f'The earned interest is {calc2:.2f}.')


print(f'The terminal value amounts to {calc1:.2f}.')
