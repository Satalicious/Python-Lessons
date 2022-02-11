#!/usr/bin/env python3

"""This module offers simple functions for interest calculation."""

"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""


def interest (capital, rate, years=1, tax=0):
     
    assert (rate<=1) and (tax<=1),'tax & rate must be between 0 and 1! Try again.'
    compint = capital*(1+rate*(1-tax))**years
    yz = compint - capital
    return f'the profit is {yz:.2f}€'


def terminal_value (capital, rate, years=1, tax=0):
    assert (rate<=1) and (tax<=1),'tax & rate must be between 0 and 1! Try again.'
    #compint = capital*(1+rate/100*(1-tax/100))**years
    compint = capital*(1+rate*(1-tax))**years
    return compint
    
#print(interest(100,0.1))
#print(terminal_value(100,0.1))