import sys

if __name__ == "__main__":
    if len(sys.argv)!=2:
        print("Not enough or too much arguments. You must specified exactly one string.")
    else:
        print(len(sys.argv[1]))