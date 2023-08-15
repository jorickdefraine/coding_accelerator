import sys

if __name__=="__main__":
    s = sys.argv[1:-1]
    separator = sys.argv[-1]
    res = separator.join(s)
    print(res)
