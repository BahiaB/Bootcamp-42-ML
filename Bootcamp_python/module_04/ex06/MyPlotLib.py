import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from FileLoader import FileLoader

class MyPlotLib:

    def histogram(data, feature):
        data[feature].hist(color = 'purple', edgecolor = 'black')
        plt.show()

    def density(data, features):
        data[features].plot.kde()
        plt.show()

    def pair_plot(data, features):
        sns.pairplot(data[features],markers=".", height=2)
        plt.show()

    def box_plot(data, features):
        sns.boxplot(data=data[features])
        plt.show()


# TESTS
'''loader = FileLoader
data = loader.load('athlete_events.csv')
mpl = MyPlotLib
mpl.histogram(data, ["Height", "Weight"])
mpl.density(data, ["Height", "Weight"])
mpl.pair_plot(data, ["Height", "Weight"])
mpl.box_plot(data, ["Height", "Weight"])'''