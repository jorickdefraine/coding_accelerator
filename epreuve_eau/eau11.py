import sys
import numpy as np

def absMinDiff(f):
    diff=[]
    for i in f:
        for j in f:
            diff.append(abs(int(i)-int(j)))

    return np.sort(list(set(diff)))[1]

if __name__=="__main__":

    f = sys.argv[1:]

    print(absMinDiff(f))