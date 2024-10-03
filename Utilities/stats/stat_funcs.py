#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Stats module for special continuous distributions."""


from math import factorial


def permutations(n, r) -> int:
    """Gets the number of permutations."""
    return factorial(n) / factorial(n - r)

def combinations(n, r) -> int:
    """Gets the number of combinations."""
    return factorial(n) / (factorial(r) * factorial(n - r))

def approximate_cdf(dist, a, b) -> float:
    """Approximates the CDF of a distribution."""
    pass