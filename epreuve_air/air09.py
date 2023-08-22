import sys

if __name__ == "__main__":
    list = sys.argv[1:]

    for elt in list[1:]:
        print(elt, end=" ")
    print(list[0])