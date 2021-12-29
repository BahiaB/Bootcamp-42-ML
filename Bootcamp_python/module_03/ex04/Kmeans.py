
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import sys



class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=0):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
          None.
        Raises:
          This function should not raise any Exception.
        """
        self.kmeans =KMeans(init="random", 
                            n_clusters=self.ncentroid, 
                            n_init=self.max_iter)
        self.kmeans.fit(X)


    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
          the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
            11
        This function should not raise any Exception """
        self.cluster_labels = self.kmeans.predict(X)
        self.centroids = self.kmeans.cluster_centers_
        print(self.centroids)
        return self.centroids

