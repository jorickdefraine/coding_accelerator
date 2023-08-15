import sys

if __name__=="__main__":

    firstString = sys.argv[1]
    secondString = sys.argv[2]

    if secondString in firstString:
        print("True")
    else:
        print("False")