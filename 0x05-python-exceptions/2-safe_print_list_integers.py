#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    element_count = 0
    try:
        while index < x:
            if type(my_list[index]) == int:
                print("{:d}".format(my_list[index]),end="")
                index += 1
                element_count += 1
            else:
                index += 1
    except ValueError as error:
        print(error)
    print()
    return element_count
