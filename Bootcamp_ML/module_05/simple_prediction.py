import numpy as np
import sys
from tools import add_intercept

def simple_predict(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray. 
    Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
        theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
        y_hat as a numpy.ndarray, a vector of dimension m * 1.
        None if x or theta are empty numpy.ndarray.
        None if x or theta dimensions are not appropriate.
    Raises:
        This function should not raise any Exception."""
    #pred = x.copy()
    #pred = lambda x: theta[0] + theta[1] * x
    
    #y_hat = pred(x)
    #print(y_hat)
    x = add_intercept(x)
    return x.dot(theta)
    
'''#test  
x = np.arange(1,6)
# test 1:
theta1 = np.array([5, 0])
print(simple_predict(x, theta1))

# test: 2
theta2 = np.array([0, 1])
print(simple_predict(x, theta2))

# test: 3
theta3 = np.array([5, 3])
print(simple_predict(x, theta3))

# test: 4
theta4 = np.array([-3, 1])
print(simple_predict(x, theta4))'''