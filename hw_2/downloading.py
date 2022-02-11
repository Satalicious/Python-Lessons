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


with urllib.request.urlopen('https://bulme.find-santa.eu/data/python/fc.txt') as f:
    html = f.read().decode('utf-8')


list = html.splitlines()

count = 0
sum = 0

for words in list:
    sv = list[count]
    count += 1
    sv = sv[-2:]
    sum += int(sv)

avg = sum/7


if avg >= 25:
    print(f'Next weekend, swimming would be a good activity.')

elif avg > 12 <= 25:
    print(f'Next weekend, hiking would be a good activity.')

elif avg > 5 <= 12:
    print(f'Next weekend, watching movies would be a good activity.')

elif avg >= -5 <= 5:
    print(f'Next weekend, relaxing in the local hot springs would be a good activity.')

elif avg < -5:
    print(f'Next weekend, skiing would be a good activity.')
