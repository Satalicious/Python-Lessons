"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

import ssl 
#sicherheitszertifikat

try:
   _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


import urllib.request 
#um url zu importieren


with urllib.request.urlopen('https://www.senarclens.eu/~gerald/teaching/cms/vrptw/r101.txt') as f:
    contents = f.read().decode('utf-8')

sum = 0
for i in range(10,717,7):
    sum = sum + float(contents.split()[i])


print("Total demand: ",sum)


