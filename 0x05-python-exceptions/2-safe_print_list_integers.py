#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
        except ValueError:
            pass
    print()

#safe_print_list_integers([1,2,3, "HY",4,5,0, "Hello"], 7)