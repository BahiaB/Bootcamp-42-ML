import sys
import string


if len(sys.argv) != 3:
    sys.exit("ERROR")
if not type(sys.argv[1]) == str:
    sys.exit("1st parameter is not a string")
try:
    sys.argv[2] = int(sys.argv[2])
    str = sys.argv[1]
    for c in string.punctuation:
        str = str.replace(c, "")
    #print(str)
    list = str.split()
    i = 0
    while i < len(list):   
        if len(list[i]) <= sys.argv[2]:
            list.pop(i)
        else: 
            i += 1
    print(list)
except ValueError:
    sys.exit("error")