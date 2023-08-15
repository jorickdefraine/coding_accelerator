import sys

if __name__=="__main__":
        f = sorted(sys.argv[1:])
        for i in f:
            print(i, end=" ")