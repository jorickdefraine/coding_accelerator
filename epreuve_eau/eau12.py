import sys
import numpy as np

def swap(k,j,f):
    index_k = f.index(k)
    index_j = f.index(j)
    f[index_k] = j
    f[index_j] = k
    return f

def myBubbleSort(f):
    for i in range(len(f)-1,0,-1):
        tableau_trie = 1
        for j in range(i):
            if int(f[j+1])<int(f[j]):
                f = swap(f[j+1],f[j],f)
                tableau_trie = 0
        if tableau_trie:
            return f
    return f

if __name__=="__main__":

    f = sys.argv[1:]

    print(myBubbleSort(f))