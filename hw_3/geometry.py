#!/usr/bin/env python3
"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""

"""Functions calculating characteristic numbers of geometric shapes."""


def perimeter_right_triangle(c1, c2):
    """
    Return the perimeter of a right triangle.

    `c1`, `c2`: catheti of the right triangle
    """
    c3 = c1 + c2
    return c3

def area_right_triangle (c1,c2):
    """
    Return the area of a right triangle.

    `c1`, `c2`: catheti of the right triangle
    """
    A = 1/2 * c1 * c2
    return A

def perimeter_circle (r):
    """
    Return the perimeter of a circle.

    `r`: radius of the circle
    """
    import math
    U = math.pi * 2 * r
    return U

def area_circle (r):
    """
    Return the area of a circle.

    `r`: radius of the circle
    """
    import math
    A = r * r * math.pi
    return A

def surface_sphere (r):
    """
    Return the surface of a sphere.

    `r`: radius of the sphere
    """
    import math
    S = 4 * math.pi * r * r
    return S

def volume_sphere (r):
    import math
    V = 4/3 * math.pi * r * r * r
    return V

def surface_cylinder (r, h):
    import math
    S = 2 * math.pi * r * r + 2 * math.pi * r * h
    return S

def volume_cylinder (r, h):
    import math
    V = math.pi * r * r * h
    return V

def surface_cone (r, h):
    import math
    S = math.pi * r * h
    return S

def volume_cone (r,h):
    import math
    V = 1/3 * math.pi * r * r * h
    return V
