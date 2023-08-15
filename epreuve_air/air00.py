import sys

def split(string, sep=" "):
    res = []
    j = 0
    for i in range(len(string)):
        if string[i]==sep:
            res.append(string[j:i])
            j = i+1
    res.append(string[j:])
    return res

if __name__=="__main__":
    s = sys.argv[1]
    res = split(s)
    for elt in res:
        print(elt)
