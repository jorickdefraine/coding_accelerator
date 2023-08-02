import sys

if __name__=="__main__":

    string=sys.argv[1].split(" ")
    result = ""
    for elt in string:
        result+=elt[0].upper()+elt[1:]+" "

    print(result)