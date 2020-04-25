"""
correlation.py
====================================
The module for fast correlation computation.
"""

import staticrab_backend as B
import numpy as np


def chatterjee(x: np.ndarray, y: np.ndarray) -> float:
    """
    Computes the Chatterjee's correlation measure.

    The function computes the Chatterjee's correlation measure.

    Parameters
    ----------
    x:
        array of float64
    y:
        array of float64, cannot be constant

    Returns
    -------
    float
        Chatterjee's correlation coefficient for x, y

    Examples
    --------

    >>> a = np.array(range(5), dtype=np.float64)
    >>> chatterjee(a, a)
    0.5
    >>> a = np.array(range(2000), dtype=np.float64)
    >>> chatterjee(a, a)
    0.9985007496251874
    """
    # TODO: Move this check to the backend
    if len(np.unique(y)) == 1:
        raise ValueError('The y cannot be constant.')
    if x.dtype != np.float64:
        raise ValueError(f"Only the dtype = np.float64 is supported. The provided x has dtype {x.dtype}.")
    if y.dtype != np.float64:
        raise ValueError(f"Only the dtype = np.float64 is supported. The provided y has dtype {y.dtype}.")

    # calling the backend function that does not do any checks
    return B.chatterjee(x, y, False)
