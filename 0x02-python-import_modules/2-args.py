#!/usr/bin/python3
def argument_count():

    import sys
    arguements = sys.argv[1:]
    if (len(arguements) > 1):
        print("{} argements: ".format(len(arguements)))
    elif (len(arguements) == 0):
        print("{} arguments. ".format(len(arguements)))
    else:
        print("{} argument: ".format(len(arguements)))
    # iterate through the arguement and print by index starting from index 1
    length = len(arguements)
    for index in range(length):
        arg = 1 + index
        print("{}: {}".format(arg, arguements[index]))


# Function call
if __name__ == "__main__":
    argument_count()
