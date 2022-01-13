"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

import math

radius = float(input("Enter the radius: "))

height = float(input("Enter the height: "))

O = 2 * math.pi * radius * height

V = (math.pi / 3) * (height ** 2) * (3 * radius - height)


print(f"The spherical cap has a surface of {O:.3f}")

print(f"The volume of the spherical cap is {V:.3f}")
