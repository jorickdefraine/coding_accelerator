import sys
#todo
if __name__=="__main__":
    # _int = int(sys.argv[-1])
    list = sys.argv[1:]
    n = len(list)
    first = []
    second = []
    for i in list:
        if i!="fusion":
            first.append(i)
        else:
            break
    for i in range(len(first)+1,n):
        second.append(list[i])

    def function(_list, _int):
        n = len(_list)
        _int = int(_int)
        new_list = []
        
        if not(_int>int(_list[-1])):
            for i in range(n-1):
                new_list.append(_list[i])
                if _int>int(_list[i]) and _int<int(_list[i+1]):
                    new_list.append(_int)
            new_list.append(_list[-1])

        else:
            for i in range(n):
                new_list.append(_list[i])
            new_list.append(_int)

        return new_list

    for i in second:
        first = function(first, i)
        
    print(first)