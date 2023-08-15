import sys

if __name__ == "__main__":
    if len(sys.argv)!=3:
        print("error")
    elif int(sys.argv[2])>0:

        print(int(sys.argv[1])**int(sys.argv[2]))
    else:
        print("error")