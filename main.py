import numpy as np
from scipy.interpolate import lagrange

def polynomial_interpolator(x_values, y_values):
    """
    Interpolates a polynomial that passes through the given points.

    Parameters:
        x_values (array_like): x-coordinates of the points.
        y_values (array_like): y-coordinates of the points.

    Returns:
        numpy.poly1d: A polynomial object representing the interpolated polynomial.
    """
    return lagrange(x_values, y_values)

# An example of its usage; feel free to change the numbers to see how it functions:
x_values = np.array([0, 1, 2, 3, 4])
y_values = np.array([1, 3, 8, 6, 2])

interpolated_polynomial = polynomial_interpolator(x_values, y_values)
print("Result:")
print(interpolated_polynomial)