"""
This module provides functions to convert between Celsius to Fahrenheit.
"""

"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""


def celsius2fahrenheit(celsius):
    """
    Convert a temperature given in Celsius to Fahrenheit.
    """
    F = (9 / 5 * celsius) + 32
    return celsius


def fahrenheit2celsius(fahrenheit):
    """
    Convert a temperature given in Fahrenheit to Celsius.
    """
    C = 5/9 * (fahrenheit - 32)
    C = round(C,2)
    return fahrenheit