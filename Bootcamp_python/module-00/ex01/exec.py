import sys

def main():
    t = ''.join(sys.argv[1::])
    print(t.swapcase()[::-1])

if __name__ == "__main__":
    main()
