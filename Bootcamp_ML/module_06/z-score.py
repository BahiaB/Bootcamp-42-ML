
import numpy as np

class TinyStatistician:

    def __init__(self):
        pass

    def mean(lst):
        if len(lst) == 0:
            return None
            print("wesh")
        res = 0
        for elem in lst:
            res =  res + elem
        res = res / len(lst)
        return(res)

    
    def median(lst):
        if len(lst) == 0:
            return None
        lst.sort()
        if len(lst) % 2 == 1:
            y = (len(lst)+1 )/ 2
            res = lst[int(y -1)]

        if len(lst) % 2 == 0:
              v1 = len(lst) / 2
              res = (lst[int(v1 -1)] + lst[int(v1)]) / 2
        return(res)

    def quartiles(lst, percentile):
        if len(lst) == 0:
            return None
        i = ((percentile / 100) * len(lst))
        lst.sort()
        return(lst[int(i)])

    def var(lst):
        #if len(lst) == 0:
        #    return(None)
        res = 0

        y =TinyStatistician.mean(lst)
        for elem in lst:
            res += (elem - y) **2 
        return(res/len(lst))

    def std(x: np.ndarray) -> float:
        return TinyStatistician.var(x) ** 0.5

def zscore(x) :
    """Computes the normalized version of a non-empty numpy.ndarray using the z-score
        standardization.
    Args:
        x: has to be an numpy.ndarray, a vector.
    Returns:
        x' as a numpy.ndarray.
        None if x is an empty numpy.ndarray.
    Raises:
        This function shouldn't raise any Exception.
    """
    mean = TinyStatistician.mean(x)
    std = TinyStatistician.std(x)
    x_prime = np.zeros(x.shape)
    for i in range(x.size):
        x_prime[i] = (x[i] - mean) / std
    return x_prime

if __name__ == "__main__":
    X = np.array([0, 15, -9, 7, 12, 3, -21])
    print(zscore(X))
        # Output:
    '''array([-0.08620324,  1.2068453 , -0.86203236,  0.51721942,  0.94823559,
        0.17240647, -1.89647119])'''
# Example 2:    
    Y = np.array([2, 14, -13, 5, 12, 4, -19])
    print(zscore(Y))
    # Output:
    '''array([ 0.11267619,  1.16432067, -1.20187941,  0.37558731,  0.98904659,
        0.28795027, -1.72770165])'''