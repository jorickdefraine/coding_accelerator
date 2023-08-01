import sys

if __name__ == "__main__":
    try:
        a,b = int(sys.argv[1]), int(sys.argv[2])
        result = a//b
        print("result:", result)
        print("reste:", a-result*b)
    except:
        print("erreur.")        
        