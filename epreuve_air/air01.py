import sys

if __name__=="__main__":
    s = sys.argv[1]
    separator = sys.argv[2]
    res = s.split(separator)
    for elt in res:
        print(elt)
