import sys
import numpy as np 


def isSorted(list1):
    list2 = np.sort(list1)

    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            return "not sorted"
    return "sorted"

print(isSorted(sys.argv[1:]))