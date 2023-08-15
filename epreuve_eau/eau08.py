import sys

def isOnlyInt(s):
    for c in s:
        try:
            tmp = int(c)
        except:
            return False
    return True

if __name__=='__main__':

    s = sys.argv[1]
    print(isOnlyInt(s))
