from matplotlib import pyplot as plt


def abline(a_coords, b_coords, ax=None, **kwargs):
    """Draw a line connecting a point `a_coords` with a point `b_coords`.

    Parameters
    ----------
    a_coords : array-like, shape (2,)
        xy coordinates of the start of the line.

    b_coords : array-like, shape(2,)
        xy coordiantes of the end of the line.

    ax : matplotlib axis
        Axe to plot the line

    **kwargs : dict
        Arguments to pass along to the matplotlib `plot` function.
    """
    if ax is None:
        ax = plt.gca()

    line_start, line_end = list(zip(a_coords, b_coords))
    line, = ax.plot(line_start, line_end, **kwargs)

    return line
