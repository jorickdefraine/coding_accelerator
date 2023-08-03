import sys


if __name__=="__main__":

    f = int(sys.argv[1])
    s = int(sys.argv[2])
    for i in range(min(f,s), max(f,s)-1):
        print(i,end=" ")
    print(max(f,s)-1)
    