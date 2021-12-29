import sys

def ft_filter(function_to_apply, list_of_inputs):
    ret = []
    for elem in list_of_inputs:
        if function_to_apply(elem) == True:
            ret.append(elem)

    return(ret)

lst = [0, 1, 2, 3, 5, 8, 13]
print(ft_filter(lambda x: x + 5 < 10 , lst))