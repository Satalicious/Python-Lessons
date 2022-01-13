"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

import cmath

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))




q = complex(cmath.sqrt((b**2) - 4 * a * c))

x1 = (-b + q) / (2 * a)
x2 = (-b - q) / (2 * a)


print (f"x1: {x1:.2f} x2: {x2:.2f}")
                                ### ergibt in dem fall das selbe wie zeile 18: 
                                ### print("{:.2f} {:.2f}".format(x1,x2))