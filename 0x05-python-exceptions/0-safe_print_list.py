#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        num_ele = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            num_ele += 1
    except IndexError:
        pass

    finally:
        print()
        return num_ele
