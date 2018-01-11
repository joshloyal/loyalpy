import numpy as np

from matplotlib import pyplot as plt
from matplotlib import patheffects


def label_line(line, label, x, y, color='0.5', size=12):
    """Add a label to a line, at the proper angle.

    Arguments
    ---------
    line : matplotlib.lines.Line2D object
        The line to which the annotation is attached
    label : str
        Label text
    x : float
        x-position to place center of text (in data coordinates)
    y : float
        y-position to place center of text (in data coordinates)
    color : str, optional (default='0.5' grey level)
        Color of text
    size : float, optional (default=12)
        Size in pt
    """
    xdata, ydata = line.get_data()
    x1 = xdata[0]
    x2 = xdata[-1]
    y1 = ydata[0]
    y2 = ydata[-1]

    ax = line.axes
    text = ax.annotate(label, xy=(x, y), xytext=(-10, 0),
                       textcoords='offset points',
                       size=size, color=color,
                       horizontalalignment='left',
                       verticalalignment='bottom')

    sp1 = ax.transData.transform_point((x1, y1))
    sp2 = ax.transData.transform_point((x2, y2))

    rise = (sp2[1] - sp1[1])
    run = (sp2[0] - sp1[0])

    slope_degrees = np.degrees(np.arctan2(rise, run))
    text.set_rotation(slope_degrees)

    return text


def label_ray(ray_xy1, ray_xy2, label, x, y, ax=None, color='0.5', size=12):
    """Add a label to an ray at the proper angle.

    Parameters
    ----------
    ray_xy1 : array-like, shape (2,)
        The starting point of the ray
    ray_xy2 : array-like, shape (2,)
        The ending point of the ray
    label : str
        Label text
    x : float
        x-position to place center of text (in data coordinates)
    y : float
        y-position to place center of text (in data coordinates)
    color : str, optional (default='0.5' grey level)
        Color of text
    size : float, optional (default=12)
        Size in pt
    """
    if ax is None:
        ax = plt.gca()

    x1, y1 = ray_xy1
    x2, y2 = ray_xy2

    text = ax.annotate(label, xy=(x, y), xytext=(-10, 0),
                       textcoords='offset points',
                       size=size, color=color,
                       horizontalalignment='left',
                       verticalalignment='bottom')

    sp1 = ax.transData.transform_point((x1, y1))
    sp2 = ax.transData.transform_point((x2, y2))

    rise = (sp2[1] - sp1[1])
    run = (sp2[0] - sp1[0])

    slope_degrees = np.degrees(np.arctan2(rise, run))
    if slope_degrees < -90:
        slope_degrees = 180 + slope_degrees
    text.set_rotation(slope_degrees)
    text.set_path_effects([
        patheffects.withStroke(linewidth=2, foreground='k')])

    return text
