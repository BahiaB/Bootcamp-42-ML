import numpy as np
from ImageProcessor import ImageProcessor
from NumPyCreator import NumPyCreator

class ColorFilter:

    def invert(array):
        return (1 - array)

    def to_blue(array):
        new = np.zeros(array.shape)
        new[:, :, 2] = array[:, :, 2]
        return (new)

    def to_green(array):
        return (array * [0, 1, 0])
    
    def to_red(self, array):
        return (array - self.to_blue(array) - self.to_green(array)) 

    def to_celluloid(array):
        temp = np.arange(0.0, 1.1, 0.1)
        for i , row in enumerate(array):
            for j ,col in enumerate(row):
                for k, rgb in enumerate(col):
                    array[i, j, k] = temp[int(array[i, j, k] * 10)]
        return(array)



    def to_grayscale(array, filter='w'):
        if filter == 'm' or filter == 'mean':
            mean = np.sum(array, axis=2) /3
            mean = np.broadcast_to(mean[..., None], array.shape)
            return(mean)
        elif filter == 'weighted' or filter == 'w' :
            w = np.sum(array * [0.299, 0.587, 0.114] ,axis=2) 
            w = np.tile(w[...,None], 3)
            return(w)

