import sys


def swap(k,j,f):
    index_k = f.index(k)
    index_j = f.index(j)
    f[index_k] = j
    f[index_j] = k
    return f

def mySelectionSort(f):
    n = len(f)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if int(f[j])<int(f[min]):
                min = j
        if min!=i:
            f = swap(f[min],f[i],f)
    return f

if __name__=="__main__":

    f = sys.argv[1:]

    print(mySelectionSort(f))