#!/usr/bin/env python3

"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

def quadratic(a, b, c):
    """Compute the solution to a quadratic equation."""
    import cmath
    root = b ** 2 - 4 * a * c
    x1 = (-b + cmath.sqrt(root)) / (2 * a)
    x2 = (-b - cmath.sqrt(root)) / (2 * a)
    return x1, x2