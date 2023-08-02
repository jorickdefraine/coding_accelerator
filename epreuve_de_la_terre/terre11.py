import sys 

if __name__ == "__main__":
    char = sys.argv[1]
    hour = int(char[:2])
    minute = char[3:5]
    if hour==0:
        print("12:"+minute+" PM")

    elif hour>12:
        new_hour = hour-12
        print(str(new_hour)+":"+minute+" PM")
    else:
        print(char+" AM")

