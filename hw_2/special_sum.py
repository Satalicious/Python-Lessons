"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""


denominator = int(input('Denominator: '))
uplimit = int(input('Upper limit: '))

sum = 0

for x in range(1,uplimit):
    if x%denominator == 0:
        sum = sum + x

print (f'Sum: {sum + uplimit}')
