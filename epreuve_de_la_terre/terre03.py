import sys


if __name__ == "__main__":
    first_letter = ord(sys.argv[1])
    result=""
    for i in range(first_letter,123):
        result+=chr(i).lower()
    print(result+"\n")

