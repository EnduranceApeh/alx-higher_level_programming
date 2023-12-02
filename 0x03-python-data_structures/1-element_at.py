#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list)
    if idx < 0 or idx >= list_len:
        return None
    else:
        lst = my_list[idx]
        return lst
