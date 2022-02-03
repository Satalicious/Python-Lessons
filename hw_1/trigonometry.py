"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

import math

radians = 0.0


print( 'radians | sine | tangent')
print('-------------------------')

while radians <= math.pi:
    
    sine = round(float(math.sin(radians)),2)                      ## variable mit sinuskurve & radians verknüft 
    tangent = round(float(math.tan(radians)),2)

    
    print("{:>7.2f} |{:>6} | {:>7}".format(radians, sine, tangent))

    radians = radians + 0.1


sine = math.sin(math.pi)                        ## variable mit sinuskurve & radians verknüft 
tangent = math.tan(math.pi)

print("{:>7.2f} |{:>6.1f} | {:>7.1f}".format(math.pi, sine, tangent))