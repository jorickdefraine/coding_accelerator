import sys

if __name__=="__main__":
    _int = int(sys.argv[-1])
    list = sys.argv[1:-1]
    n = len(list)
    
    for i in range(n-1):
        print(list[i], end=" ")
        if _int>int(list[i]) and _int<int(list[i+1]):
            print(_int, end=" ")
    print(list[-1])