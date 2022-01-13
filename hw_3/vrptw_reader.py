#!/usr/bin/env python3

"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

"""Functions for reading and working with VRPTW text input files."""



def read_string_list(x='r101'):
    y = x[-4:]
    if y != '.txt':
        x = x + '.txt'
    with open('r101.txt', 'r') as f:
        txt = f.read()
        r = txt.splitlines()[1:]
    return r

print(read_string_list('r101.txt'))


def get_demand(x, no):
    customer = no - 1

    c_data = x[customer]

    sheet = c_data.split()
    return float(sheet[3])

print(get_demand(read_string_list('r101'),10))


    

    


