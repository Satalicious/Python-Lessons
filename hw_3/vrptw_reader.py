#!/usr/bin/env python3

"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

"""Functions for reading and working with VRPTW text input files."""




def read_string_list(x='r101'):
    from os import path

    file_path=path.abspath(__file__) #path holen
    dir_path=path.dirname(file_path) #directory holen
    x = dir_path + '/' + 'r101.txt'
    y = x[-4:]
    if y != '.txt':
        x = x + '.txt'
    with open(x, 'r') as f:
        txt = f.read()
        r = txt.splitlines()[1:]
    return r

#print(read_string_list('r101.txt'))


def get_demand(x, no):
    customer = no - 1
    c_data = x[customer]
    sheet = c_data.split()
    return float(sheet[3])

def calc_distance(x,no,no2):
    import numpy as np
    customer = no - 1
    customer2 = no2 - 1
    c_data = x[customer]
    c2_data = x[customer2]
    sheet = c_data.split()
    sheet2 = c2_data.split()
    sheet = float(sheet[3])
    sheet2 = float(sheet2[3])
    dist = np.linalg.norm(sheet-sheet2)
    return dist


#print(get_demand(read_string_list(),2))
#print(calc_distance(read_string_list(),2,3))

    

    


