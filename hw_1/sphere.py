"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

import math

radius = float(input("Enter a radius: "))

area = 4 * math.pi * radius**2
volume = 4 / 3 * math.pi * radius**3

print(f"The sphere has a volume of {volume:.2f}")
print(f"The surface area of this sphere is {area:.2f}")


