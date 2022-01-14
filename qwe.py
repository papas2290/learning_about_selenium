lst = [1, 2, 3, 4, 5, 6]


def modify_list(l):

    for el in l:
        # print(el)
        if el % 2 == 0:
           l.append(el//2)
        else:
            l.pop(el)
    return l


print(modify_list(lst))
