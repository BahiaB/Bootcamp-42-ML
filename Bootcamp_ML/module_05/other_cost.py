import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt

def mse_(y, y_hat):
    j = len(y)
    mse = np.sum((y_hat - y) **2 ) / j
    return mse

def rmse_(y, y_hat):
   
    rmse = mse_(y, y_hat) ** 0.5
    return (rmse)

def mae_(y, y_hat):

    j = len(y)
    mae = np.sum(abs(y_hat - y) / j)
    return (mae)

def r2score_(y, y_hat):
    #R2= 1- SSres / SStot
    j = len(y)
    mean = np.sum(y)/ j
    r2 = 1 - (np.sum((y_hat - y) **2 ) / j) / (np.sum((y - mean) **2 ) / j)
    return(r2)


x = np.array([0, 15, -9, 7, 12, 3, -21])
y = np.array([2, 14, -13, 5, 12, 4, -19])
print(mse_(x,y))
# Output: 4.285714285714286
print(rmse_(x,y))
## Output: 2.0701966780270626

print(mae_(x, y))
#1.7142857142857142

print(r2score_(x,y))
print(r2_score(x,y))
## Output:0.9681721733858745