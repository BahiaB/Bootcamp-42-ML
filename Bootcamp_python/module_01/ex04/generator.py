
import sys
import random

def generator(text, sep=" ", option=None):
    

    if not isinstance(text, str) or not isinstance(sep, str) or option==None:
        yield ("ERROR")
        return
    
    lst = text.split(sep)
    print(lst)

    if option == "ordered":
        lst.sort()
    elif option == "unique":
        lst= list(set(lst))
    elif option == "shuffle":
       if (option == 'shuffle'):
        lst.sort(key=lambda x: random.random())



    for i in (lst) :
        yield (i)
    
