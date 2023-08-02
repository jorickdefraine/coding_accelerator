import sys

def isPrime(n):
    if n>1:
        for i in range(2, n//2+1):
            if n%i==0:
                return "{} is not a prime number.".format(n)
        return "{} is a prime number.".format(n)
    else:
        return "{} is not a prime number.".format(n)

if __name__ == "__main__":
    print(isPrime(int(sys.argv[1])))