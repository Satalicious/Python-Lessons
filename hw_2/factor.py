"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

number = int(input('Integer: '))
number2 = number
factors = []


while number % 2 == 0:
    factors.append(2)
    number = number / 2
while number % 3 == 0:
    factors.append(3)
    number = number / 3
while number % 5 == 0:
    factors.append(5)
    number = number / 5
while number % 7 == 0:
    factors.append(7)
    number = number / 7
while number % 11 == 0:
    factors.append(11)
    number = number / 11


listToStr = ' * '.join(map(str, factors))

print(f'{number2} = {listToStr}')
