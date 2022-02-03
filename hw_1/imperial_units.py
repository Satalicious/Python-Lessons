"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

inp = float(input('Enter a distance in meters: '))



inch = inp * 39.37
feet = inp * 39.37 / 12 
yard = feet / 3
mile = yard / 1760

inch = round(inch,2)
feet = round(feet,2)
yard = round(yard,2)
mile = round(mile,3)

print(str(inch) + ' inch')
print(str(feet) + ' feet')
print(str(yard) + ' yards')
print(f"{mile:.2f} miles")