"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

from os import path

file_path = path.abspath(__file__) #path holen
dir_path = path.dirname(file_path) #directory holen
dir_path1 = dir_path + '/' + 'rot13.txt'


with open (dir_path1) as f:
    txt = f.read()

def convert(txt):
    list1 = []
    list1[:0] = txt.upper()
    return list1

txt_upper = convert(txt)

f_half = 'ABCDEFGHIJKLM'
s_half = 'NOPQRSTUVWXYZ'

result = "File to decode: "

for char in txt_upper:
    if char in f_half:
        result += chr(ord(char)+13)
    if char in s_half:
        result += chr(ord(char)-13)
    if len(char) == 11:
        result += "\n"
    elif char == '-':
        result += '-'
    elif char == ' ':
        result += ' '

print(result)

