import numpy as np


class MyLinearRegression: 
    """
    Description:
    My personnal linear regression class to fit like a boss."""
    pass

    def __init__(self, thetas, alpha=0.001, max_iter=1000): 
        if isinstance(thetas, list):
            thetas = np.asarray(thetas)
        #thetas = thetas.astype("float64")
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas


    def add_intercept(self,x, theta):
        
        ones = np.ones((x.shape[0], 1))
        res = np.concatenate((ones, x), axis=1)
        
        return(res)
    
    def predict_(self,x):

        theta = self.thetas
        x = self.add_intercept(x, theta)
        y_hat = x.dot(theta)
        return y_hat


    def cost_elem_(self,y , y_hat):
        y_hat = y_hat.reshape(-1, 1)
        j = (y_hat -  y) ** 2
        return(j)

    def cost_(self, y, y_hat):
        j = self.cost_elem_(y, y_hat)
        if j is None:
            return None
        jv = self.cost_elem_(y, y_hat)
        jv = jv / (2* y.shape[0])
        return np.sum(jv)

    def gradient(self,x, y, theta):
        self.thetas = self.thetas.reshape(-1, 1)
        x_prime = self.add_intercept(x, theta)

        y_hat = self.predict_(x)
        x_transpose = np.transpose(x_prime)
        #print(x_prime)
        #print(x_transpose)
        size = len(x)
        res = x_transpose.dot(y_hat- y)
        res /= size
        return(res)


    def fit_(self, x, y):
        theta = self.thetas
        new_theta = np.ndarray
        #print(x)
        #print(y)
        #print(theta)
        while self.max_iter >= 0:
            new_theta = self.gradient(x,y, theta)
            #if self.max_iter == 1500000:
            #   print(new_theta)
            theta[0] -= self.alpha * new_theta[0]
            theta[1] -= self.alpha * new_theta[1]
            self.max_iter -= 1
        self.thetas = theta
        return(theta)

    def mse_(self,y, y_hat):
        j = len(y)
        mse = np.sum((y_hat - y) **2 ) / j
        return mse


MyLR= MyLinearRegression


x = np.array([[12.4956442], [21.5007972],
            [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236],
            [45.7655287], [46.6793434], [59.5585554]])


theta = np.array([2, 0.7])

x = x.reshape(len(x), 1)
y = y.reshape(len(y), 1)
theta = theta.reshape(len(theta), 1)

lr1 = MyLR(theta)

print(lr1.mse_(x, y))

    # Example 0.0:
print(lr1.predict_(x))
    # Output:
"""
    array([[10.74695094],
           [17.05055804],
           [24.08691674],
           [36.24020866],
           [42.25621131]])
"""

    # Example 0.1:
print(lr1.cost_elem_(y,lr1.predict_(x)))
    # Output:
"""
    array([[710.45867381],
       [364.68645485],
       [469.96221651],
       [108.97553412],
       [299.37111101]])
"""

    # Example 0.2:
#print("ici")
print(lr1.cost_(lr1.predict_(x), y))
    # Output:
"""
    195.34539903032385
"""

    # Example 1.0:
lr2 = MyLR([1.0, 1.0], 5e-8, 1500000)
#print("lr2.fit =")
print(lr2.fit_(x, y).reshape(-1,1))

#print(lr2.thetas)
    # Output:
"""
    array([[1.40709365],
           [1.1150909]])
"""

    # Example 1.1:
print(lr2.predict_(x).reshape(-1, 1))
    # Output:
"""
    array([[15.3408728],
           [25.38243697],
           [36.59126492],
           [55.95130097],
           [65.53471499]])
"""

    # Example 1.2:
print(lr2.cost_elem_(y, lr2.predict_(x)))
    # Output:
"""
    array([[486.66604863],
       [115.88278416],
       [ 84.16711596],
       [ 85.96919719],
       [ 35.71448348]])
"""

    # Example 1.3:
print(lr2.cost_(y, lr2.predict_(x)))
    # Output:
"""
    80.83996294128525
"""