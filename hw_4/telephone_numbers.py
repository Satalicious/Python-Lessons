#!/usr/bin/env python3

"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

def as_numeric(text):
    """
    testdoc
    """
    out_list = []
    i=0
    text = list(text.upper())
    output=""
    conv = {"A":2, "B":2, "C":2,"D":3, "E":3,"F":3,"G":4,"H":4,"I":4,"J":5,"K":5,"L":5,"M":6,"N":6,
    "O":6,"P":7,"Q":7,"R":7,"S":7,"T":8, "U":8, "V":8,"W":9, "X":9, "Y":9,"Z":9}
    val_list = list(conv.values())
    key_list = list(conv.keys())
    position = key_list.index("R")
    print(val_list[position])
    print(key_list[position])

    for i in range(len(text)):
        if text[i] in key_list:
            position = conv[text[i]]
            out_list.append(val_list[position])
        else:
            out_list+=text[i]
    print(out_list)
    for ele in range(len(out_list)):
        if type(out_list[ele]) == str:
            output+=out_list[ele]
        else:
            continue
    print(output)

print(as_numeric('0800 reimann'))

"""
    for i in range(len(text)):
        for key, value in conv.items():
            if text[i] == value:
                out.append()
    print(out)
"""