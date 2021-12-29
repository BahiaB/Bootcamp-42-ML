import sys
class Vector:

    def __init__(self, *arg):
        self.values = []
        self.size = 0

        if len(arg) < 1 or len(arg) > 1:
            sys.exit("ERROR")
        if isinstance(arg[0], list):
            for i in arg[0]:
                self.values.append(float(i))
            self.size = len(self.values)
        elif isinstance(arg[0], int):
            self.size = arg[0]
            for i in range(0 , self.size):
                self.values.append(float(i))
        elif isinstance(arg[0], tuple):
            for i in range(arg[0][0], arg[0][1]):
                self.values.append(float(i))
            self.size = len(self.values) 
        
    def __add__(self, num):
        new_v = Vector(self.values)
        if isinstance(num, int):
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] + num
        elif isinstance(num, Vector):
            if len(new_v.values) != len(num.values):
                sys.exit("ERROR")
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] + num.values[i]
        else:
            sys.exit("ERROR")
        return new_v
    
    def __sub__(self, num):   
        new_v = Vector(self.values)
        if isinstance(num, int):
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] - num
        elif isinstance(num, Vector):
            if len(new_v.values) != len(num.values):
                sys.exit("ERROR")
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] - num.values[i]
        else:
            sys.exit("ERROR")
        return new_v 

    def __mul__(self, num):
        new_v = Vector(self.values)
        y = 0
        if isinstance(num, int):
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] * num
            return new_v
        elif isinstance(num, Vector):
            if len(new_v.values) != len(num.values):
                sys.exit("ERROR")
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] * num.values[i]
            for i in range(self.size):
                y = y + new_v.values[i]
        else:
            sys.exit("ERROR")
        return y

    def __truediv__(self, num):
        if num == 0:
            sys.exit(" div by 0 = impossible")
        new_v = Vector(self.values)
        if isinstance(num, int):
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] / num
        return new_v
         
    def __radd__(self, num):
        new_v = Vector(self.values)
        if isinstance(num, int):
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] + num
        elif isinstance(num, Vector):
            if len(new_v.values) != len(num.values):
                sys.exit("ERROR")
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] + num.values[i]
        else:
            sys.exit("ERROR")
        return new_v
            
    def __rsub__(self, num):   
        new_v = Vector(self.values)
        if isinstance(num, int):
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] - num
        elif isinstance(num, Vector):
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] - num.values[i]
        else:
            sys.exit("ERROR")
        return new_v 

    def __rtruediv__(self, num):
        if num == 0:
            sys.exit(" div by 0 = impossible")
        new_v = Vector(self.values)
        if isinstance(num, int):
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] / num
        return new_v

    def __mul__(self, num):
        new_v = Vector(self.values)
        y = 0
        if isinstance(num, int):
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] * num
            return new_v
        elif isinstance(num, Vector):
            if len(new_v.values) != len(num.values):
                sys.exit("ERROR")
            for i in range(self.size):
                new_v.values[i] = new_v.values[i] * num.values[i]
            for i in range(self.size):
                y = y + new_v.values[i]
        else:
            sys.exit("ERROR")
        return y


            

