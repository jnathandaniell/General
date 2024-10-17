#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""3d surface plotter."""


from matplotlib import pyplot as plt


def get_surface_plot(xyz: tuple, **kwargs):
    """Plots a surface given a vertically stacked xyz vector."""
    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    x, y, z = xyz[0], xyz[1], xyz[2]
    # Options.
    for key, val in kwargs.items():
        match key:
            case 'labels':
                ax.set_xlabel(val[0])
                ax.set_ylabel(val[1])
                ax.set_zlabel(val[2])
            case 'angle':
                ax.view_init(elev=val[0], azim=val[1], roll=val[2])
            case _:
                pass
    ax.plot_trisurf(x, y, z)
    return fig