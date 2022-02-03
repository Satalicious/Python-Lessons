"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""


Fahrenheit = float(input('Enter a temperature in degrees Fahrenheit: '))

C = 5/9 * (Fahrenheit - 32)

C = round(C,2)

print(str(Fahrenheit) + ' degrees Fahrenheit correspond to ' + str(C) + ' degrees Celsius')
