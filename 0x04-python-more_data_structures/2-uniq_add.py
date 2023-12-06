#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    # Convert list to set
    unique_num = set(my_list)
    for num in unique_num:
        sum += num
    return sum
