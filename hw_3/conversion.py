"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

def celsius2fahrenheit(celsius):
    """
    Convert a temperature given in Celsius to Fahrenheit.
    """
    F = (9 / 5 * celsius) + 32
    return F


def fahrenheit2celsius(fahrenheit):
    """
    Convert a temperature given in Fahrenheit to Celsius.
    """
    C = 5/9 * (fahrenheit - 32)
    return C

