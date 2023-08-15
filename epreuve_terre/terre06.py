import sys

if __name__ == "__main__":

    if len(sys.argv)<2:
        print('Not enough arguments. You must specified a string.')
    elif len(sys.argv)>=3:
        print('Too much arguments.')
    else:
        char = sys.argv[1]
        n = len(char)
        new_char = ""
        for i in range(n):
            new_char += char[n-i-1]
        print(new_char)
