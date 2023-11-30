#!/usr/bin/python3
import sys
arguements = sys.argv[1:]
if __name__ == "__main__":
    if (len(arguements) > 1):
        print("{} arguments: ".format(len(arguements)))
    elif (len(arguements) == 0):
        print("{} arguments. ".format(len(arguements)))
    else:
        print("{} argument: ".format(len(arguements)))
    # iterate through the arguement and print by index starting from index 1
    length = len(arguements)
    for index in range(length):
        arg = 1 + index
        print("{}: {}".format(arg, arguements[index]))
