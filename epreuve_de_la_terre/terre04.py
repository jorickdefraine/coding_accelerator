import sys

if __name__ == "__main__":
    try:
        nb = int(sys.argv[1])
        if nb==0:
            print("pair et impair")
        elif not(nb%2):
            print("pair")
        else:
            print("impair")
    except:
        print("Tu ne me la mettras pas à l'envers.")        
        