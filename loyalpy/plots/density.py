import matplotlib.pyplot as plt
import numpy as np
import numbers
import scipy.linalg as linalg

from matplotlib.patches import Ellipse


__all__ = ['normal_contour']


def normal_contour(mean, cov, n_std=2, ax=None, **kwargs):
    if cov.shape[0] != 2:
        raise ValueError('Only for bivariate normal densities.')

    eigenvalues, eigenvectors = linalg.eigh(cov)

    # sort the eigenvalues and eigenvectors in descending order
    order = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[order]
    eigenvectors = eigenvectors[:, order]

    # determine the angle of rotation
    angle = np.degrees(np.arctan2(*eigenvectors[:, 0][::-1]))

    if ax is None:
        ax = plt.gca()

    if isinstance(n_std, numbers.Integral):
        # the diameter of the ellipse is twice the square root of the evalues
        width, height = 2 * n_std * np.sqrt(eigenvalues)
        ellipse = Ellipse(xy=mean, width=width, height=height, angle=angle,
                          **kwargs)
        ax.add_artist(ellipse)

        return ellipse

    ellipses = []
    for std in n_std:
        width, height = 2 * std * np.sqrt(eigenvalues)
        ellipse = Ellipse(xy=mean, width=width, height=height, angle=angle,
                          **kwargs)

        ax.add_artist(ellipse)
        ellipses.append(ellipse)

    return ellipses
