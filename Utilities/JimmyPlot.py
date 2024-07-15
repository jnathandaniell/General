#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple plotting module to make Jimmy's life easier.
"""

__author__ = "James Daniell"
__copyright__ = ""
__credits__ = ["James Daniell"]
__license__ = ""
__version__ = "0.1"
__maintainer__ = "James Daniell"
__email__ = "jnathandaniell@gmail.com"
__status__ = "Development"


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np


def plot_data(data: tuple, labels: list, log = False) -> Figure:
    """Creates a plot for X and Y data provided as tuple."""
    fig, ax = plt.subplots()
    ax.plot(data[0], data[1])
    ax.set(xlabel=labels[0], ylabel=labels[1], title=labels[2])
    if log:
        plt.yscale("log")
    plt.show()
    return fig

def multiplot_data(plots:tuple, legend:list, labels:list, log=False) -> Figure:
    """Plots multiple sets of data on the same graph, given as a tuple of tuples."""
    fig, ax = plt.subplots()
    # Plot each set of X,Y coordinates
    for i in plots:
        ax.plot(i[0], i[1])
    # Set legend and labels
    ax.legend(legend, loc=1)
    ax.set(xlabel=labels[0], ylabel=labels[1])
    if log:
        plt.yscale("log")
    plt.show()
    return fig

def plot_vstacked(plots:tuple, labels:list) -> Figure:
    """Plots n sets of data as vertically stacked plots."""
    fig, axs = plt.subplots(len(plots), sharex=True)
    # Plot each set of X,Y coordinates
    for i in range(len(plots)):
        axs[i].plot(plots[i][0], plots[i][1])
        axs[i].set_ylabel(labels[i])
    fig.text(0.5, 0.04, labels[-1], ha='center')
    plt.show()
    return fig

def multiplot_vstacked(plots:tuple, legend:list, labels:list) -> Figure:
    """Plots n sets of data of multiple lines as vertically stacked plots."""
    fig, axs = plt.subplots(len(plots), sharex=True)
    # Plot each set of X,Y coordinates
    for i in range(len(plots)):
        for j in range(len(plots[i])):
            axs[i].plot(plots[i][j][0], plots[i][j][1])
            axs[i].set_ylabel(labels[i])
    # Set legend and labels
    axs[0].legend(legend, loc=1)
    fig.text(0.5, 0.04, labels[-1], ha='center')
    plt.show()
    return fig

def plot_surface(X:np.ndarray, Y:np.ndarray, Z:np.ndarray) -> Figure:
    """Plots a 3d surface given X, Y, and Z meshes."""
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # surf = ax.plot_surface(X, Y, Z)
    plt.show()
    return fig

def save_figure(fig:Figure, filepath:str):
    """Saves figure to file location."""
    fig.savefig(filepath)