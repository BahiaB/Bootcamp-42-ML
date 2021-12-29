import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from FileLoader import FileLoader


class Komparator:
    def __init__(self, data):
        self.data = data

    def compare_box_plots(self,categorical_var, numerical_var):

        fig, axs = plt.subplots(nrows=1, ncols=2)
        sns.boxplot(x =self.data[numerical_var][self.data[categorical_var]== 'F'], ax =axs[0], color="purple")
        axs[0].set_title('Female graph')
        sns.boxplot(x =self.data[numerical_var][self.data[categorical_var]== 'M'], ax =axs[1])
        axs[1].set_title('Male graph')
        plt.show()

    def compare_histograms(self,categorical_var, numerical_var):
        fig, axs = plt.subplots(nrows=1, ncols=2)
        axs[0].hist(self.data[numerical_var][self.data[categorical_var]== 'F'],20, color="purple", edgecolor = 'black',alpha=0.75)
        axs[0].set_title('Female graph')
        axs[1].hist(self.data[numerical_var][self.data[categorical_var]== 'M'],20, edgecolor = 'black',alpha=0.75)
        axs[1].set_title('Male graph')

        plt.show()

    def density(self,categorical_var, numerical_var):
        sns.kdeplot(self.data[numerical_var][self.data[categorical_var] == 'F'], label="Femme", color="purple")
        sns.kdeplot(self.data[numerical_var][self.data[categorical_var] == 'M'], label="Homme")
        plt.legend(loc = 'upper left')
        plt.title('density graph', loc='center')
        plt.show()

