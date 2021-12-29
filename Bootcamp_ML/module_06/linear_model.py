import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt

def plot(Xpill, Yscore,y_hat):
    axes = plt.axes()
    plt.xlabel("Quantity of blue pill (in micrograms)")
    plt.ylabel("Space driving score")
    axes.grid()
    #y_hat = predict_(Xpill)
    plt.scatter(Xpill, Yscore)
    plt.plot(Xpill, y_hat,"--X", color='green')
    plt.show()

    

'''def plot_cost(x, y, y_hat):
    axes = plt.axes()
    axes.grid()
    linear_model = MyLR(np.array([[0], [0]]), max_iter=500)
    thetas0 = range(85, 95, 2)
    theta1 = np.linspace(-0.2,1,50)
    epsilon = pow(10,-6)
    for t0 in epsilon:
        linear_model.thetas[0][0] = t0'''
        




data = pd.read_csv("are_blue_pills_magic.csv")
Xpill = np.array(data["Micrograms"]).reshape(-1,1)
Yscore = np.array(data["Score"]).reshape(-1,1)
linear_model1 = MyLR(np.array([[89.0], [-8]]))
linear_model2 = MyLR(np.array([[89.0], [-6]]))
Y_model1 = linear_model1.predict_(Xpill)
Y_model2 = linear_model2.predict_(Xpill)
linear_model = MyLR(np.array([[89.0],[-8]]), max_iter=500)
linear_model = MyLR(np.array([[89.0], [-8]]), max_iter=500)

linear_model.fit_(Xpill,Yscore)
y_hat = linear_model.predict_(Xpill)
plot(Xpill, Yscore, y_hat)
#plot_cost(Xpill, Yscore, y_hat)
print(linear_model1.mse_(Yscore, Y_model1))
print(f' by Sklearn ={mean_squared_error(Yscore, Y_model1)}')
print(linear_model2.mse_(Yscore, Y_model2))
print(f' by Sklearn ={mean_squared_error(Yscore, Y_model2)}')