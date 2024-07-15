#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Error module for quick calculation of error and error statistics.
"""

__author__ = "James Daniell"
__copyright__ = ""
__credits__ = ["James Daniell"]
__license__ = ""
__version__ = "0.2"
__maintainer__ = "James Daniell"
__email__ = "jnathandaniell@gmail.com"
__status__ = "Development"



class PointError:
    """Class for calculating error at a single point.
    
    Allows calculation of error between a forecasted and actual value based
    on some of the standard error types common in data analysis. User may
    select the error type, and error is calculated automatically if provided
    at initialization.
    """
    def __init__(self, x=0., y=0., err_type=None) -> None:
        """Initialize with forcast (x) and actual (y) then calculate error."""
        self.x = x
        self.y = y
        self.err_type = err_type
        self.calc_error()
    
    def __str__(self) -> str:
        """Show user error type and error."""
        output = "Type:" + str(self.err_type)   \
                 + ", Error=" + str(self.error)
        return output

    def calc_err(self) -> float:
        """Calculate direct error."""
        return self.y - self.x
    
    def calc_abs_err(self) -> float:
        """Calculate absolute error."""
        return abs(self.y - self.x)

    def calc_sq_err(self) -> float:
        """Calculate squared error."""
        from math import pow
        return pow(self.calc_err(), 2.)

    def calc_ape(self) -> float:
        """Calculate absolute percentage error."""
        if self.y == 0.:
            return 1.
        else:
            return abs((self.y - self.x) / self.y) * 100.
    
    def calc_error(self) -> None:
        """Calculate and set class error based on provided error type."""
        match self.err_type:
            case "abs":
                self.error = self.calc_abs_err()
            case "sq":
                self.error = self.calc_sq_err()
            case "ape":
                self.error = self.calc_abs_err()
            case _:
                self.error = self.calc_err()
    
    def update_err_type(self, err_type) -> None:
        """Updates error type and recalculates error."""
        self.set_err_type(err_type=err_type)
        self.calc_error()

    def set_x(self, x) -> None:
        """Sets the forecast value."""
        self.x = x
    
    def set_y(self, y) -> None:
        """Sets the actual value."""
        self.y = y

    def set_err_type(self, err_type) -> None:
        self.err_type = err_type

    def get_error(self) -> float:
        """Return the calculated error."""
        return self.error



class SeriesError():
    """Class for calculating error and error statistics with a series of data.

    Operates using lists and inherits from errors calculated by the PointError
    class. Creates a list of PointErrors and calculates statistics from the
    errors recieved, treated as a distribution. Provide with a forecasted
    values list and actual values list as well as error type to immediately
    generate calculations.
    """
    def __init__(self, X=[], Y=[], err_type=None) -> None:
        """Initialize with forcasted dataset (X), actual dataset (Y), and error type, then calculate errors, sum, mean, standard deviation, and standard error."""
        self.X = X
        self.Y = Y
        self.N = self.__len__()
        self.err_type = err_type
        self.get_point_errors()
        self.calc_errors()
        self.calc_stats()
    
    def __len__(self) -> int:
        """Gets length of PointError list."""
        return len(self.point_errors)

    def __str__(self) -> str:
        """Show user error type, number of samples, mean, and stdev."""
        output = "Type:" + str(self.err_type)   \
                 + ", N=" + str(self.N) \
                 + ", Mean=" + str(self.mean)   \
                 + ", Stdev=" + str(self.stdev)
        return output
    
    def get_point_errors(self) -> None:
        """Make a list of PointErrors for error calculation."""
        self.point_errors = [PointError(x, y, err_type=self.err_type) 
                             for x,y in zip(*self.X, *self.Y)]
    
    def calc_errors(self) -> None:
        """Calculate errors from PointError list."""
        self.errors = [err.get_error() for err in self.point_errors]
    
    def calc_sum(self) -> None:
        """Calculate sum of errors."""
        self.sum = sum(self.errors)

    def calc_mean(self) -> None:
        """Calculate mean of errors."""
        from math import inf
        try:
            self.mean = self.sum / self.N
        except ValueError:
            print("No values detected.")
            self.mean = inf
    
    def calc_stdev(self) -> None:
        """Calculate standard deviation of errors."""
        from math import sqrt, pow, inf
        squares = [pow(err - self.mean, 2) for err in self.errors]
        try:
            self.stdev = sqrt(sum(squares) / self.N)
        except ValueError:
            print("No values detected.")
            self.stdev = inf
    
    def calc_stderr(self) -> None:
        """Calculate standard error of errors."""
        from math import sqrt, inf
        try:
            self.stderr = self.stdev / sqrt(self.N)
        except ValueError:
            print("No values detected.")
            self.stderr = inf

    def calc_stats(self) -> None:
        """Calculates basic statistics from error series."""
        self.calc_sum()
        self.calc_mean()
        self.calc_stdev()
        self.calc_stderr()

    def update_error(self, err_type=False) -> None:
        """Updates error from PointError objects for series."""
        if not err_type:
            pass
        else:
            self.set_err_type(err_type=err_type)
        for e in self.point_errors:
            e.update_err_type(self.err_type)
        self.calc_stats()
    
    def get_errors(self) -> list:
        """Return the calculated list of errors."""
        return self.errors
    
    def get_sum(self) -> float:
        """Return the calculated sum."""
        return self.sum
    
    def get_mean(self) -> float:
        """Return the calculated mean."""
        return self.mean
    
    def get_stdev(self) -> float:
        """Return the calculated standard deviation."""
        return self.stdev
    
    def get_stderr(self) -> float:
        """Return the calculated standard error."""
        return self.stderr
    
    def set_xy(self, X, Y) -> None:
        self.X = X
        self.Y = Y
    
    def set_err_type(self, err_type) -> None:
        self.err_type = err_type