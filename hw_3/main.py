
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
import vrptw_reader


if __name__ == '__main__':
    def main():
        print("vrptw_reader.read_string_list(); expected:     1      35.00      35.00       0.00       0.00     230.00       0\n",
        vrptw_reader.read_string_list())

        print("addition.sum_to(10) expected: 55",
        addition.sum_to(10))
        import equations
    