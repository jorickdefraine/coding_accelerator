import sys

if __name__=="__main__":
    ops = sys.argv[-1]
    list = sys.argv[1:-1]
    for elt in list:
        if ops[0]=="+":
            print(int(elt)+int(ops[1:]), end=" ")
        else:
            print(int(elt)-int(ops[1:]), end=" ")

    print()