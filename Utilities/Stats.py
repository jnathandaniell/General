#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Stats module for simple calculations of basic distribution statistics.
"""

__author__ = "James Daniell"
__copyright__ = ""
__credits__ = ["James Daniell"]
__license__ = ""
__version__ = "0.1"
__maintainer__ = "James Daniell"
__email__ = "jnathandaniell@gmail.com"
__status__ = "Development"


def get_perumutations(n, r):
    """"""
    from math import factorial
    return round(factorial(n) / factorial(n-r))

# SimpleStats class for single population basic statistics.
class SimpleStats():
    """Class for producing simple summary statistics.

    Recieves dataset as a list and calculates summary statistics using the
    'calc_basic_stats' function. Statistical information may be retrieved
    after this function is called.
    """

    def __init__(self, X=[]):
        """Takes a dataset and calculates standard statistical mesaures."""
        self.X = X
        self.N = self.__len__()
        self.calc_basic_stats()
    
    def __len__(self):
        """Gets numer of samples in dataset."""
        return len(self.X)
    
    def calc_basic_stats(self) -> None:
        """Calculates basic statistics, passes if empty dataset."""
        if self.N > 0:
            self.calc_sum()
            self.calc_mean()
            self.calc_median()
            self.calc_mode()
            self.calc_range()
            self.calc_stdev()
            self.calc_var()
            self.calc_stderr()
        else:
            pass

    def calc_sum(self):
        """Calculate sum of dataset."""
        self.sum = sum(self.X)

    def calc_mean(self) -> None:
        """Calculate mean of dataset."""
        from math import inf
        try:
            self.mean = self.sum / self.N
        except ValueError:
            print("No values detected.")
            self.mean = inf
    
    def calc_stdev(self) -> None:
        """Calculate standard deviation of dataset."""
        from math import sqrt, pow, inf
        squares = [pow(x - self.mean, 2) for x in self.X]
        try:
            self.stdev = sqrt(sum(squares) / self.N)
        except ValueError:
            print("No values detected.")
            self.stdev = inf
    
    def calc_var(self) -> None:
        from math import pow
        self.var = pow(self.stdev, 2)
    
    def calc_stderr(self) -> None:
        """Calculate standard error of dataset."""
        from math import sqrt, inf
        try:
            self.stderr = self.stdev / sqrt(self.N)
        except ValueError:
            print("No values detected.")
            self.stderr = inf
    
    def calc_range(self) -> None:
        """Calculate range of dataset."""
        self.range =  max(self.X) - min(self.X)

    def calc_median(self) -> None:
        """Calculate median of dataset."""
        X = sorted(self.X)
        if self.N % 2 == 0:
            self.median = (X[int(self.N / 2.) - 1] + X[int(self.N / 2.)]) / 2.
        else:
            self.median = X[int(self.N / 2.)]

    def calc_mode(self) -> None:
        """Finds mode of dataset."""
        d = {}
        for x in self.X:
            d[x] += 1
        k = d.keys()
        c = 0
        mode = 0
        for key in k:
            if d[k] > c:
                c = d[k]
                mode = k
        self.mode = mode
    
    def calc_percentile(self, percentile) -> float:
        """Calculates the kth percentile of the dataset."""
        X = sorted(self.X)
        ind = round(self.N * percentile / 100)
        return X[ind]
    
    def calc_pct_of_val(self, val) -> float:
        """Calculates the percentile of a given value."""
        X = sorted(self.X)
        for i in range(self.N):
            if X[i] > val:
                pass
            else:
                if i != self.N:
                    return (i + 0.5) / self.N * 100.
        return 100.

