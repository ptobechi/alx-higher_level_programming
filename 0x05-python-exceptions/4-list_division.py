#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for element in range(list_length):
        try:
            result = my_list_1[element] / my_list_2[element]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    # print(new_list)
    return new_list
            
# my_l_1 = [10, 8, 4]
# my_l_2 = [2, 4, 4]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)

# print("--")

# my_l_1 = [10, 8, 4, 4]
# my_l_2 = [2, 0, "H", 2, 7]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)


