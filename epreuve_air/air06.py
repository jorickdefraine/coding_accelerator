import sys

if __name__=="__main__":
    char = sys.argv[-1]
    list = sys.argv[1:-1]
    for elt in list:
        if not(char.lower() in elt.lower()):
            print(elt,end=" ")
    print()