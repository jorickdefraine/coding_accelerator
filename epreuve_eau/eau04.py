import sys

def isPrime(n):
    if n<=1: return False
    for i in range(2, n//2):
        if not(n%i):
            return False
    return True

def firstPrimeNumber(n):
    i=n
    while not(isPrime(i)):
        i+=1
    return i

if __name__=="__main__":
    n=int(sys.argv[1])

    print(firstPrimeNumber(n))