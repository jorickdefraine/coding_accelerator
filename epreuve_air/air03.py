import sys

if __name__=="__main__":
    s = sys.argv[1:]

    cnt=0
    for i in s:
        for j in s:
            if i==j:
                cnt+=1
        if cnt==1:
            print(i)
        cnt=0

    