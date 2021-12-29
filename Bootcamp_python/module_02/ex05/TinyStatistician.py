import sys

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

if __name__ == "__main__":
    t = TinyStatistician

    a = [1, 42, 300, 10, 59]
    b = [24, 23 , 25, 28, 30, 18, 26, 27]

    #print(t.mean(a))
    #print(t.median(b))
    #print(t.median(a))
    #print(t.quartiles(a, 25))
    print(t.var(a))
        
