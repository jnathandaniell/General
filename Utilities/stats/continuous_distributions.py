#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Stats module for special continuous distributions."""


from math import pow, exp, sqrt, pi, gamma


class Uniform():
    """Uniform distribution."""

    a = 0.
    b = 1.

    def __init__(self, a=a, b=b) -> None:
        self.a = a
        self.b = b

    def pdf(self) -> float:
        """Return pdf at x."""
        return 1 / (self.b - self.a)

    def mean(self) -> float:
        """Return mean of distribution."""
        return (self.a + self.b) / 2

    def var(self) -> float:
        """Return variance of distribution."""
        return pow((self.b - self.a), 2) / 12

    def mgf(self, t) -> float:
        """Return moment generating function evaluated at t."""
        return (exp(self.b * t) - exp(self.a * t)) / ((self.b - self.a) * t)


class Normal():
    """Normal distribution."""

    mu = 0
    sig = 1

    def __init__(self, mu=mu, sig=sig) -> None:
        self.mu = mu
        self.sig = sig
    
    def pdf(self, x) -> float:
        """Return pdf at x."""
        a = 1 / (sqrt(2 * pi) * self.sig)
        b = exp(-pow((x - self.mu) / self.sig, 2) / 2)
        return a * b
    
    def mean(self) -> float:
        """Return mean of distribution."""
        return self.mu
    
    def var(self) -> float:
        """Return variance of distribution."""
        return pow(self.sig, 2)
    
    def mgf(self, t) -> float:
        """Return moment generating function evaluated at t."""
        return exp(self.mu * t + pow(self.sig, 2) * pow(t, 2) / 2)


class Gamma():
    """Gamma distribution."""

    theta = 1
    k = 1

    def __init__(self, theta=theta, k=k) -> None:
        self.theta = theta
        self.k = k
    
    def pdf(self, x) -> float:
        """Return pdf at x."""
        a = 1 / (self.theta * gamma(self.k))
        b = pow(x, self.k - 1)
        c = exp(-x / self.theta)
        return a * b * c
    
    def mean(self) -> float:
        """Return mean of distribution."""
        return self.k * self.theta
    
    def var(self) -> float:
        """Return variance of distribution."""
        return self.k * pow(self.theta, 2)
    
    def mgf(self, t)  -> float:
        """Return moment generating function evaluated at t."""
        return pow((1 / (1 - self.theta * t)), self.k)


class Exponential():
    """Exponential distribution."""

    theta = 1

    def __init__(self, theta=theta) -> None:
        self.theta = theta
    
    def pdf(self, x) -> float:
        """Return pdf at x."""
        return (1 / self.theta) * exp(-x / self.theta)
    
    def mean(self) -> float:
        """Return mean of distribution."""
        return self.theta
    
    def var(self) -> float:
        """Return variance of distribution."""
        return pow(self.theta, 2)
    
    def mgf(self, t) -> float:
        """Return moment generating function evaluated at t."""
        return 1 / (1 - self.theta * t)


class TwoParamExp():
    """Two-Parameter Exponential distribution."""

    theta = 1
    nu = 0

    def __init__(self, theta=theta, nu=nu) -> None:
        self.theta = theta
        self.nu = nu
    
    def pdf(self, x) -> float:
        """Return pdf at x."""
        return (1 / self.theta) * exp(-(x - self.nu) / self.theta)
    
    def mean(self) -> float:
        """Return mean of distribution."""
        return self.nu + self.theta
    
    def var(self) -> float:
        """Return variance of distribution."""
        return pow(self.theta, 2)
    
    def mgf(self, t) -> float:
        """Return moment generating function evaluated at t."""
        return exp(self.nu * t) / (1 - self.theta * t)


class DoubleExp():
    """Double Exponential distribution."""

    theta = 1
    nu = 0

    def __init__(self, theta=theta, nu=nu) -> None:
        self.theta = theta
        self.nu = nu
    
    def pdf(self, x) -> float:
        """Return pdf at x."""
        return (1 / (2 * self.theta)) * exp(-abs(x - self.nu) / self.theta)
    
    def mean(self) -> float:
        """Return mean of distribution."""
        return self.nu
    
    def var(self) -> float:
        """Return variance of distribution."""
        return 2 * pow(self.theta, 2)
    
    def mgf(self, t) -> float:
        """Return moment generating function evaluated at t."""
        return exp(self.nu * t) / (1 - pow(self.theta, 2) * pow(t, 2))


class Weibull():
    """Weibull distribution."""

    theta = 1
    beta = 1

    def __init__(self, theta=theta, beta=beta) -> None:
        self.theta = theta
        self.beta = beta
    
    def pdf(self, x) -> float:
        """Return pdf at x."""
        a = self.beta / pow(self.theta, self.beta)
        b = pow(x, self.beta - 1)
        c = exp(-pow(x / self.theta, self.beta))
        return a * b * c
    
    def mean(self) -> float:
        """Return mean of distribution."""
        try:
            x = self.theta * gamma(1 + 1 / self.beta)
        except:
            x = None
        return x
    
    def var(self) -> float:
        """Return variance of distribution."""
        pass

