#!/usr/bin/env python3

"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

def as_numeric(text):
    """
    Enter string to convert into numeric values for telephone keypad
    """
    out_list = []
    i=0
    text = list(text.upper())
    output=""
    conv = {"A":2, "B":2, "C":2,"D":3, "E":3,"F":3,"G":4,"H":4,"I":4,"J":5,"K":5,"L":5,"M":6,"N":6,
    "O":6,"P":7,"Q":7,"R":7,"S":7,"T":8, "U":8, "V":8,"W":9, "X":9, "Y":9,"Z":9}
    key_list = list(conv.keys())
    
    for i in range(len(text)):
        if text[i] in key_list:
            position = conv[text[i]]
            out_list.append(position)
        else:
            out_list+=text[i]

    for ele in range(len(out_list)):
        output+=str(out_list[ele])
    print(output)
    return output

if __name__ == "__main__":
    print(as_numeric('0664 abcdefghijklmnopqrstuvwxyz'))
