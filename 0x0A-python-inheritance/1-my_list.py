#!/usr/bin/python3

"""The 1-my_list has the function: print_sorted(self)"""


class MyList(list):
    """The class MyList that inherits from list"""

    def print_sorted(self):
        """Function that prints the list, but sorted (ascending sort)"""

        print(sorted(self))
