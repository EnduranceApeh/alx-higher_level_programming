#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    # Loop through list to check if it's divisible by 2
    for number in my_list:
        if number % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
