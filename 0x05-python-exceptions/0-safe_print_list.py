#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_elements = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed_elements += 1
    except IndexError:
        pass
    finally:
        print()
    return printed_elements


count = safe_print_list(my_list=[1, 2,3,"safe"], x=10)
print(count)