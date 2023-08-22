import sys

if __name__ == "__main__":
    arg = sys.argv[1:]
    symbol = arg[0]
    height = int(arg[1])
    length = height*(3)
    for i in range(height):
        line = " "*(round((length)/2)-i)+(2*i+1)*symbol
        print(line)
