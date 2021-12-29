import sys

def ft_map(function_to_apply, list_of_inputs):
    ret = []
    for elem in list_of_inputs:
        ret.append(function_to_apply(elem))
    return(ret)



lst = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
print(list(ft_map(lambda x: x + 2 , lst)))

