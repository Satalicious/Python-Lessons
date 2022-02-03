#!/usr/bin/env python3

"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""
"""Functions to en-/decode a string using the rot13 algorithm."""


def encode(inp):
    text = inp.upper()
    result = ""
    f_half = "ABCDEFGHIJKLM"
    s_half = "NOPQRSTUVWXYZ"
    for char in text:
        if char in f_half:
            result += chr(ord(char)+13)
        if char in s_half:
            result += chr(ord(char)-13)
        elif char == '-':
            result += '-'
        elif char == ' ':
            result += ' '
        elif char == '.':
            result += '.'
        elif char == "'":
            result += "'"
    return result
    

print(encode('''Arire gehfg n cebtenz lbh qba'g unir fbheprf sbe.'''))


def decode(inp):
    text = inp.upper()
    result = ""
    f_half = 'ABCDEFGHIJKLM'
    s_half = 'NOPQRSTUVWXYZ'
    for char in text:
        if char in f_half:
            result += chr(ord(char)+13)
        if char in s_half:
            result += chr(ord(char)-13)
        elif char == '-':
            result += '-'
        elif char == ' ':
            result += ' '
        elif char == '.':
            result += '.'
        elif char == "'":
            result += "'"
    return result


print(decode("NEVER TRUST A PROGRAM YOU DONT HAVE SOURCES FOR."))
