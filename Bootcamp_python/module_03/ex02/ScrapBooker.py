import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpltimg
from NumPyCreator import NumPyCreator as npc
from ImageProcessor import ImageProcessor

class ScrapBooker:

    def crop(array, dimensions, position=(0,0)):
        img = array
        if (img.shape[0] >= dimensions[0] + position[0] or
            img.shape[1] >= dimensions[1] + position[1]):
            i = img[position[0]: dimensions[0] + position[0], position[1]: dimensions[1] + position[1]]
            return(i)
        else:
             sys.exit("ERROR")

    
    def thin(array, n, axis):
        array = np.delete(array, np.s_[n-1::n], axis)
        return array


    def juxtapose(array, n, axis):
        copy = np.copy(array)
        for i in range(n):
            copy = np.concatenate((array, copy), axis)
        return(copy)

    def mosaic(self, array, dimensions):
        res = self.juxtapose(array, dimensions[0] - 1, 0)
        res = self.juxtapose(res, dimensions[1] - 1, 1)
        return res


