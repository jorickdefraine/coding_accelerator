

if __name__ == "__main__":

    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if i*10+j<k*10+l:
                        print(str(i)+str(j)+" "+str(k)+str(l))
