import numpy as np
import sys

#print(np.asarray(([1,2,3], [4,5,6])))
class   NumPyCreator:
    
    def from_list(lst):
        return(np.asarray(lst))
        
    def from_tuple(tpl):
        return(np.asarray(tpl))

    def from_iterable(itr):
        return(np.fromiter(itr, float))

    def from_shape(shape, value=0):
        return(np.full(shape, value))

    def random(shape):
        return(np.random.random(shape))

    def identity(n):
        return(np.eye(n))

npc = NumPyCreator
a = ([[1,2,3],[4,5,6]])
b = ("a", "b", "c")
shape=(3,5)
i = 4
print(npc.from_list(b))
print(npc.from_tuple(b))
print((npc.from_iterable(range(5))))
print(npc.from_shape(shape))
print(npc.random(shape))
print(npc.identity(i))
print((npc.identity(i)))
