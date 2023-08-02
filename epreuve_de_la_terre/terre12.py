import sys

if __name__ == "__main__":

    char = sys.argv[1]
    tod = char[-2:]
    hour = int(char[:2])
    minute = char[3:5]
    if tod=="PM":
        if hour!=12:
            new_hour = hour+12
            print(str(new_hour)+":"+minute)
        else:
            print("00:"+minute)

    else:
        print(char[:-2])
