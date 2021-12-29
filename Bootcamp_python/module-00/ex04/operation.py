import sys

if len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
    i = int(sys.argv[1])
    y = int(sys.argv[2])
    print(i + y)
    print(i - y)
    print(i * y)
    if (y == 0):
        print("quotient:     ERROR (div by zero)")
        print("remainder:    ERROR (modulo by zero)")
    else:
        print("quotient = {}".format(i/ y))
        print("remainder = {}".format(i % y))
else:
    if (len(sys.argv) == 2):
        print("Error: too few arguments")
    if (len(sys.argv) > 3):
        print("Error: too many arguments")