import sys

def ft_reduce(function_to_apply, list_of_inputs):
    ret = list_of_inputs[0]
    for elem in list_of_inputs[1 :]:
        ret = function_to_apply(ret, elem)
    return (ret)


lst = [5, 8, 10, 20, 50]
print (ft_reduce((lambda x, y: x + y), lst))

