#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sphere data generator."""


import numpy as np
from math import sqrt, pow


def build_mesh(r: float, n: int) -> tuple:
    """Builds a meshgrid with x and y coordinates."""
    x = np.linspace(0, r, n)
    y = np.linspace(0, r, n)
    return np.meshgrid(x, y)

def reshape_mesh(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Reshapes mesh to an x/y array."""
    return np.vstack((x.flatten(), y.flatten()))

def get_z(x: float, y: float, r: float) -> float:
    """Calculates z of a sphere."""
    if pow(x, 2) + pow(y, 2) <= r:
        return sqrt(pow(r, 2) - (pow(x, 2) + pow(y, 2)))
    else:
        return -1.

def get_xyz(xy_array: np.ndarray) -> np.ndarray:
    """Gets an x/y/z vector with valid values."""
    get_z_vect = np.vectorize(get_z)
    r = np.max(xy_array)
    x = xy_array[0,:]
    y = xy_array[1,:]
    z = get_z_vect(x, y, r)
    xyz_array = np.vstack((xy_array, z))
    return xyz_array[:, xyz_array[-1,:] >= 0.]

def build_local_sphere(r: float, n: int) -> np.ndarray:
    """Builds a sphere end-to-end."""
    x, y = build_mesh(r, n)
    xy = reshape_mesh(x, y)
    return get_xyz(xy)

def add_noise(xyz: np.ndarray, mu=0., sigma=1, err=0.05) -> np.ndarray:
    """Adds standard normal noise to a sphere."""
    rng = np.random.default_rng()
    z = xyz[-1,:]
    noise = rng.normal(mu, sigma, z.size)
    noisy_z = z + noise * z * err
    return np.vstack((xyz[:-1,:], noisy_z))

#######################
##### Full Sphere #####
#######################
def build_hemi_mesh(r: float, n: int) -> tuple:
    """Builds a hemisphere meshgrid with x and y coordinates."""
    half_n = int(n/2)
    x = np.linspace(-r, r, half_n)
    y = np.linspace(-r, r, half_n)
    return np.meshgrid(x, y)

def reshape_full_mesh(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Reshapes the full mesh to x/y/loc."""
    x = x.flatten()
    y = y.flatten()
    top = np.ones(shape=x.shape)
    bottom = np.zeros(shape=x.shape)
    x = np.hstack((x, x))
    y = np.hstack((y, y))
    loc = np.hstack((top, bottom))
    return np.vstack((x, y, loc))

def get_z_full(x: float, y: float, loc: bool, r: float) -> float:
    """Gets a complete sphere (not just 1/8)."""
    if pow(x, 2) + pow(y, 2) <= r:
        if loc:
            return sqrt(pow(r, 2) - (pow(x, 2) + pow(y, 2)))
        else:
            return -sqrt(pow(r, 2) - (pow(x, 2) + pow(y, 2)))
    else:
        # Dummy output to be removed.
        return np.inf

def get_full_xyz(xy_array: np.ndarray) -> np.ndarray:
    """Gets an x/y/z vector with valid values."""
    get_z_vect = np.vectorize(get_z_full)
    r = np.max(xy_array)
    x = xy_array[0,:]
    y = xy_array[1,:]
    loc = xy_array[2,:]
    z = get_z_vect(x, y, loc, r)
    xyz_array = np.vstack((xy_array, z))
    return xyz_array[:, xyz_array[-1,:] != np.inf]

def build_full_sphere(r: float, n: int) -> np.ndarray:
    """Builds a sphere end-to-end."""
    x, y = build_hemi_mesh(r, n)
    xy = reshape_full_mesh(x, y)
    return get_full_xyz(xy)

##########################
##### Builder Helper #####
##########################
def build_sphere(r: float, n: int, full=False):
    """Helper function for building a sphere."""
    if full:
        return build_full_sphere(r, n)
    else:
        return build_local_sphere(r, n)