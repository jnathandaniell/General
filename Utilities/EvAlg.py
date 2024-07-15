#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Basic functionality for individuals, evaluation, and control of EAs.
"""

__author__ = "James Daniell"
__copyright__ = ""
__credits__ = ["James Daniell"]
__license__ = ""
__version__ = "0.1"
__maintainer__ = "James Daniell"
__email__ = "jnathandaniell@gmail.com"
__status__ = "Development"



class EvMap():
    """Individual which to map MCNP to sensor results.
    
    Current format: [scaling factor], [coefficient], [inclusion types]
    """
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return ''
    
    # Evaluation methods.
    def evaluate(self) -> None:
        pass

    # Manipulation methods.
    def mutate(self) -> None:
        pass

    def mutate_mask(self) -> None:
        pass

    # Getters / setters.
    def set_shape(self, shape:tuple) -> None:
        self.shape = shape