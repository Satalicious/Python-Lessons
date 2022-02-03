"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""


Celsius = -16 ## -16, sonst wird -15 übersprungen
Ausgabe = 5



while Ausgabe >= 5:
    Celsius += 1
    Ausgabe = (9 / 5 * Celsius) + 32
    Ausgabe = round(Ausgabe,2)

    print(Celsius,' C => ' ,Ausgabe, ' F')
    if Ausgabe >= 95:
        break 
    