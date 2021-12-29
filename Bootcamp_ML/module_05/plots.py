import numpy as np
import matplotlib.pyplot as plt
from vec_cost import cost_

def plot_with_cost(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray. 
    Args:  
      x: has to be an numpy.ndarray, a vector of dimension m * 1.
      y: has to be an numpy.ndarray, a vector of dimension m * 1.
      theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
        Nothing.
    Raises:
      This function should not raise any Exception."""


    plt.plot(x, y, "o")
    h = lambda x: theta[0] + theta[1] * x
        
    plt.plot(x, h(x))
    y_hat = h(x)
    c =cost_(y, y_hat) * 2
    plt.title("Cost: %f" %c)

    #print(x)
    #print(y)
    #print(y_hat)
    for i, ax in enumerate(x):
        #print(list(ax) * 2)
        plt.plot(list(ax) * 2, [y[i], y_hat[i]], "r--")
    plt.show()



x = np.arange(1,6).reshape(5, 1)
print(type(x[0]))
y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568]).reshape(5, 1)
# Example 1:
theta1= np.array([18,-1]).reshape(2, 1)
#plot_with_cost(x, y, theta1)


theta2 = np.array([14, 0])
plot_with_cost(x, y, theta2)
