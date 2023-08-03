import sys

def findIndex(target, f):
    for i in range(len(f)):
        if f[i]==target:
            return i
    return -1

if __name__=="__main__":

    f = sys.argv[1:-1]
    target = sys.argv[-1]

    print(findIndex(target,f))