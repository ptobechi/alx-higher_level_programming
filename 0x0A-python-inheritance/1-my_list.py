#!/usr/bin/python3

"""
A module that demostrates a Class that inherites from the builtin list class
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

# my_list = MyList()
# my_list.append(1)
# my_list.append(4)
# my_list.append(2)
# my_list.append(3)
# my_list.append(5)
# print(my_list)
# my_list.print_sorted()
# print(my_list)
