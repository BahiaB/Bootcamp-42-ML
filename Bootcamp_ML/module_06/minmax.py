import numpy as np

def minmax(x):      
    
    Max = np.max(x)
    Min = np.min(x)
    dif = Max - Min
    x_prime = np.zeros(x.shape)
    size = len(x)
    for i in range(size):
        x_prime[i] = (x[i] - Min) / dif
    return x_prime


X = np.array([0, 15, -9, 7, 12, 3, -21])
print(minmax(X))
# Output:
'''array([0.58333333, 1.        , 0.33333333, 0.77777778, 0.91666667,
       0.66666667, 0.        ])'''

Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(minmax(Y))
# Output:
'''array([0.63636364, 1.        , 0.18181818, 0.72727273, 0.93939394,
      0.6969697 , 0.        ])'''