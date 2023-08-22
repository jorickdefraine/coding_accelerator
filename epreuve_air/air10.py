import sys

if __name__ == "__main__":
    file = sys.argv[1:][0]

    with open(file) as f:
        lines = f.readlines()[0]
        print(lines)