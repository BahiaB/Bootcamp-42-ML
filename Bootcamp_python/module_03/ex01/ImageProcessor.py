
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image as im

class ImageProcessor:
    
    def load(path):
        if os.path.exists(path):
            ret = plt.imread(path)
            #ret = np.asarray(img)
            print(f' loading img of dimension {ret.shape[0]}, {ret.shape[1]}')
            return (ret)
        else:
           return(None)

    def display(array):
        plt.imshow(array)
        plt.show()

imp = ImageProcessor
arr = imp.load("./resources/42AI.png")
print((arr))
imp.display(arr)
