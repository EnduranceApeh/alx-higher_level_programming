#!/usr/bin/python3
def multiple_returns(sentence):
    string_len = len(sentence)
    # check if string is empty
    if string_len == 0:
        first_char = None
        len_firstchar = (string_len, first_char)
    # if string is nor empty
    else:
        first_char = sentence[0]
        len_firstchar = (string_len, first_char)
    # return string len and first char
    return len_firstchar
