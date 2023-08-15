import sys

if __name__=="__main__":
    s = sys.argv[1]
    res=""

    for i in range(len(s)):
        if s[i]==s[i-1]:
            pass
        else:
            res+=s[i]

    print(res)