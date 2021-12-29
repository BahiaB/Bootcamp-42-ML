import sys

class Matrix:

    def __init__(self, *arg):
        self.data = []
        if isinstance(arg[0], list):
            self.data = arg[0]
            self.shape = (len(self.data), len(self.data[0]))
            #print((self.shape))
        elif isinstance(arg[0], tuple):
            self.shape = arg[0]
            for i in range(self.shape[0]):
                self.data = self.data + [[0] * self.shape[1]] 
        elif isinstance(arg[1], int):
            self.data = arg[0]
            self.shape = (len(self.data), len(self.data[0]))

    
    def __add__(self, num):
        new_m = Matrix(self.shape)
        if num.shape != self.shape:
            sys.exit("ERROR")
        if isinstance(num, Matrix):
            for i in range(new_m.shape[0]):
                for j in range(new_m.shape[1]):
                    new_m.data[i][j] = self.data[i][j] + num.data[i][j]
        return new_m

    
    def __sub__(self, num):
        new_m = Matrix(self.shape)
        if num.shape != self.shape:
            sys.exit("ERROR")
        if isinstance(num, Matrix):
            for i in range(new_m.shape[0]):
                for j in range(new_m.shape[1]):
                    new_m.data[i][j] = self.data[i][j] - num.data[i][j]
        return new_m   
        
    def __truediv__(self, num):
        if  not  isinstance(num, (int, float)):
            sys.exit("ERROR")
        new_m = Matrix(self.data)
        new_m.shape = self.shape
        for i in range(new_m.shape[0]):
            for j in range(new_m.shape[1]):
                new_m.data[i][j] = new_m.data[i][j] / num
        return new_m
    
    def __mul__(self, num):
        if isinstance(num , Matrix):
            new_m = Matrix(self.data)
            size = self.shape[1]
            for i in range(new_m.shape[0]):
                for j in range(self.shape[1]):
                    for k in range(self.shape[1]):
                        new_m.data[i][j] = sum([self.data[i][k] * num.data[k][j]])
        #print(new_m.data)
        return(new_m)
        
         
