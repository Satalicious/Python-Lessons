"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

celsius = -20
fahrenheit = -10

inp = input("For C => F enter C, for F => C enter F: ")

if inp == "C":

    while celsius <= 40:
        fahrenheit = (9/5) * celsius + 32
        print(f"{celsius} C => {fahrenheit:.1f} F")
        celsius +=1


elif inp == "F":

    while fahrenheit <= 110:
        celsius = 5/9 * (fahrenheit - 32)
        fahrenheit = (9/5) * celsius + 32
        print(f"{fahrenheit:.1f} F => {celsius:.1f} C")
        fahrenheit +=1
        

###elif inp != "C,F":                         #fleißaufgabe

  ###print("Try again, enter C or F!")
