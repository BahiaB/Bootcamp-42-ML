import sys

i = (sys.argv[1])

if  len(sys.argv) != 2 or not i.isdigit():
    print("ERROR")
else :
    i = int(i)
    if i == 0:
        print("I'm zero")
    elif i % 2 == 0:
        print("I'm even")
    else:
        print("I'm odd")
    SystemExit()