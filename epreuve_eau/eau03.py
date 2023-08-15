import sys
# 0, 1, 1, 2, 3, 5, 8, 13

def fibonacci(n):
    if n<0:
        res="error. {} is negative.".format(n)

    elif n==0:
        res=0
    else:
        u0=0
        u1=1
        for i in range(n-1):
            res=u0+u1
            u0=u1
            u1=res
            
    return res

if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))