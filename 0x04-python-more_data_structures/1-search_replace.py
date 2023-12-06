#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    # replace number if number == replace and append to newlist
    for number in my_list:
        if number == search:
            new_list.append(replace)
        else:
            new_list.append(number)
    return new_list
