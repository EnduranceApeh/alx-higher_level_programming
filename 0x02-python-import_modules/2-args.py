#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguements = sys.argv[1:]
    if (len(arguements) > 1):
        print("{} arguements: ".format(len(arguements)))
    elif (len(arguements) == 0):
        print("{} arguements. ".format(len(arguements)))
    else:
        print("{} arguement: ".format(len(arguements)))
    # iterate through the arguement and print by index starting from index 1
    length = len(arguements)
    for index in range(length):
        arg = 1 + index
        print("{}: {}".format(arg, arguements[index]))
