#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None

    le = 0
    for i, j in enumerate(my_list):
        if (le == len(my_list) - 1):
            res = my_list[i]
            break

        if (j > my_list[i + 1]):
            my_list[i + 1] = j
            res = j

        le += 1

    return res
