import numpy as np


def add_intercept(x):
    
    ones = np.ones((x.shape[0], 1))
    res = np.concatenate((ones, x), axis=1)
    return res


def predict_(x, theta):
    x = add_intercept(x)
    return x.dot(theta)
    


x = np.arange(1,6).reshape(5, 1)


'''   # Example 1:
theta1 = np.array([5, 0])
print(predict_(x, theta1))
    # Ouput: array([5., 5., 5., 5., 5.])
    # Do you understand why y_hat contains only 5's here?

    # Example 2:
theta2 = np.array([0, 1])
print(predict_(x, theta2))
    # Output: array([1., 2., 3., 4., 5.])
    # Do you understand why y_hat == x here?

    # Example 3:
theta3 = np.array([5, 3])
print(predict_(x, theta3))
    # Output: array([ 8., 11., 14., 17., 20.])

    # Example 4:
theta4 = np.array([-3, 1])
#print(predict_(x, theta4))
    # Output: array([-2., -1.,  0.,  1.,  2.])

    # More:
#print(predict_(np.array([[1, 2, 3], [4, 5, 6]]), theta4))
    # Wrong shape'''