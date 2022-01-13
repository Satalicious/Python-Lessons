"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""


uplimit = int(input('Upper limit: '))

for x in range(0,uplimit):
    if (x %2 == 0):
        if (x**2 < uplimit):
            print(x **2)
            if (x**2) >= uplimit:
                break
    
