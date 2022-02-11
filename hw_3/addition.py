#!/usr/bin/env python3

"""
This module provides a function to sum all numbers from 0 up to a given integer.
"""


def sum_to(num):
    """
    Sum all numbers from 0 up to an given integer.
    """
    assert num >= 0
    cnt=0
    for i in range(num):
        cnt+=i
    total = cnt + num
    return total
#print(sum_to(-1))
