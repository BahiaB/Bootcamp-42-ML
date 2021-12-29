import numpy as np
import sys

def add_intercept(x):
    """Adds a column of 1's to the non-empty numpy.ndarray x. Args:
      x: has to be an numpy.ndarray, a vector of dimension m * 1.
    Returns:
      X as a numpy.ndarray, a vector of dimension m * 2.
      None if x is not a numpy.ndarray.
      None if x is a empty numpy.ndarray.
    Raises:
      This function should not raise any Exception."""

    '''print(x.shape)
    if len(x.shape) !=2 :
        c= x.reshape(-1,1)
    else :'''
    '''c =x.copy()
    c = np.insert(c, 0, 1., axis=1)
    return(c)'''
    shape = (x.shape[0], 1)
    ones = np.full(shape, 1)
    res = np.concatenate((ones, x), axis=1)
    return res


'''x = np.arange(1,6)
print(add_intercept(x))


y = np.arange(1,10).reshape((3,3))
print(add_intercept(y))'''