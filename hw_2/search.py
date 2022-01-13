"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

from os import path

file_path = path.abspath(__file__) #path holen
dir_path = path.dirname(file_path) #directory holen

o = input('Files: ')

o1, o2 = o.split(',')

dir_path1 = dir_path + '/'+o1   #directory den pfad /f1.txt zuweisen
dir_path2 = dir_path + '/'+o2

count = 0

needle = input('Needle: ')

with open (dir_path1,'r') as f:
    contents1 = f.read()

with open (dir_path2,'r') as f:
    contents2= f.read()

count1 = contents1.lower().count(needle.lower())
count2 = contents2.lower().count(needle.lower())
 

count = count1 + count2



print(f'Occurrences: {count}')

