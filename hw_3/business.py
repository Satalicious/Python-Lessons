#!/usr/bin/env python3

"""This module offers simple functions for interest calculation."""

"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""


def interest (capital, rate, years=1, tax=0):
    int(years)
    if (rate<=1) and (tax<=1):
        y = (capital * (1 + (rate / 100))**years) * (1- (tax/100))
        yz = y - capital
        return print(f'the profit is {yz:.2f}€')
    else:
        return print('tax & rate must be between 0 and 1! Try again.')



def terminal_value (capital, rate, years=1, tax=0):
    int(years)
    if (rate<=1) and (tax<=1):
        y = (capital * (1 + (rate / 100))**years) * (1- (tax/100))
        return print(f'the total amount is {y:.2f}')
    else:
        return print('tax & rate must be between 0 and 1! Try again.')