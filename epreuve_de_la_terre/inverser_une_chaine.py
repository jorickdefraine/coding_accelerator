import sys

if __name__ == "__main__":

    char = sys.argv[1]
    n = len(char)
    new_char = ""

    for i in range(n):
        new_char += char[n-i-1]
    
    print(new_char)