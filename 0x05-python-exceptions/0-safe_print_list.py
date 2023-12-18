#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element_count = 0
    index = 0
    try:
        while index < x:
            print(my_list[index], end="")
            index += 1
            element_count += 1
    except IndexError:
        pass
    print()
    return element_count
