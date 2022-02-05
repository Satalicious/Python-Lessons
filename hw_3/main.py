
"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

#!/usr/bin/env python3

"""Main module of this homework."""
import equations
import addition
import conversion
import geometry
import business
import rot13
from rot13 import *


def main():
    encode('das ist das haus')

    print("addition.sum_to(10) expected: 55",
    addition.sum_to(10))
    

if __name__ == '__main__':
    main()