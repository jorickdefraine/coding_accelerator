import sys

if __name__=="__main__":
    str_ = sys.argv[1]
    result=""
    cnt=1
    for elt in str_:
        if elt.isalpha():
            cnt+=1
            if not(cnt%2) and not(elt.isupper()):
                result+=elt.upper()
            else:
                result+=elt                
        else:
            result+=elt
        
    print(result)