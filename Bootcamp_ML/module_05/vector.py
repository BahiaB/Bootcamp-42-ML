import sys
class Vector:

    def __init__(self, *arg):
        self.values = []
        i = 0
        for elem in arg[0]:
            i += 1
            if isinstance(elem, float):
                i = -1
            self.values.append(elem)
        if i == -1:
            self.shape = (1, len(self.values))
        else:
            self.shape = (i , 1)


        if len(arg) > 1 or len(arg) < 1:
            sys.exit("ERROR")
        if isinstance(self.values, list):
            self.size = len(self.values)
            

    
        

    def __str__(self):
        new_string = ''
        for value in self.values:
            if not new_string:
                new_string= 'vector [' + str(value)
            else:
                new_string += ', ' + str(value)
        if new_string:
            new_string += ']'
        return(new_string)


    
    def __add__(self, num):
        new_v = []
        if isinstance(num, int):
            if isinstance(self.values[0],list):
                for i in range(self.shape[0]):
                    new_list = []
                    new_list.append((self.values[i][0] + num))
                    new_v.append(new_list)
                return new_v
            elif isinstance(self.values[0], float):
                for i in range(self.shape[1]):
                    new_v.append((self.values[i] + num))
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

    
    
    
            
    


v1 = Vector([[5.0], [8.0]])
v2 = Vector([[2.6], [2.0]])

v3 = Vector([5.0, 8.0])
v4 = Vector([2.6, 2.0])

print(v2.shape)
print(v3 + 5)
#print(v3.shape)
