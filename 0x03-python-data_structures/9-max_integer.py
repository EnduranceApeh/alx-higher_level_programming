#!/usr/bin/python3
def max_integer(my_list=[]):
    # check if list is not empty
    if not my_list:
        return None
    else:
        max_value = my_list[0]
        # iterate through my_list ans store max value in var max_value
        for num in my_list:
            if num > max_value:
                max_value = num
        return max_value
