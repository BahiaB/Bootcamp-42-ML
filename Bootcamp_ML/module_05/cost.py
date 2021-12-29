import numpy as np
from simple_prediction import simple_predict as predict
import matplotlib.pyplot as plt
from tools import add_intercept

def cost_elem_(y, y_hat):
    """
    Description:
        Calculates all the elements (y_pred - y)ˆ2 of the cost function.
    Args:
      y: has to be an numpy.ndarray, a vector.
      y_hat: has to be an numpy.ndarray, a vector.
    Returns:
        J_elem: numpy.ndarray, a vector of dimension (number of the training examples,1).
        None if there is a dimension matching problem between X, Y or theta.
        None if any argument is not of the expected type.
    Raises:
        This function should not raise any Exception."""

    #print(f'y = {y}, yshape= , {y.shape}')
    #print(f'y_^ = {y_hat}, y^shape=  {y_hat.shape}')
    if y.shape != y_hat.shape:
        return None
    j = (y_hat -  y) ** 2#/ (2* y.shape[0])
    return(j)

def cost_(y, y_hat): 
    """
        Description:
        Calculates the value of cost function.
        Args:
        y: has to be an numpy.ndarray, a vector.
        y_hat: has to be an numpy.ndarray, a vector.
        Returns:
        J_value : has to be a float.
        None if there is a dimension matching problem between X, Y or theta.
        None if any argument is not of the expected type.
        Raises:
        This function should not raise any Exception."""
    
    j = cost_elem_(y, y_hat)
    if j is None:
        return None
    jv = np.sum(j, axis=0) / (2* y.shape[0])
    return(jv)


#exemple 1:
x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
y_hat1 = predict(x1, theta1)
y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
#print(y_hat1)

#print(cost_elem_(y1, y_hat1))
print(cost_(y1, y_hat1))

#exemple2
x2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
theta2 = np.array([[0.05], [1.], [1.], [1.]])
y_hat2 = predict(x2, theta2)

y2 = np.array([[19.], [42.], [67.], [93.]])
print(cost_elem_(y2, y_hat2))
print(cost_(y2, y_hat2))

#exemple #
x3 = np.array([0, 15, -9, 7, 12, 3, -21]).reshape(7, 1)
theta3 = np.array([[0.], [1.]])
y_hat3 = predict(x3, theta3)
y3 = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(7, 1)

#print(cost_elem_(y3, y_hat3))
print(cost_(y3, y_hat3))