#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Basic data handling utilities.
"""

__author__ = "James Daniell"
__copyright__ = ""
__credits__ = ["James Daniell"]
__license__ = ""
__version__ = "0.1"
__maintainer__ = "James Daniell"
__email__ = "jnathandaniell@gmail.com"
__status__ = "Development"



# Standard functions.
def interpolate(p1:tuple, p2:tuple, x:float) -> tuple:
    """Simple nD interpolation, based on 0th index."""
    d = tuple(a-b for a, b in zip(p1, p2))
    dx = x - p1[0]
    df = dx / d[0]
    return tuple(df * i + j for i, j in zip(d, p1))