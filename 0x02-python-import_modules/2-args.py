#!/usr/bin/python3
import sys


def argument_count():
    length = len(sys.argv)
    i = 1
    argu = length - 1

    if length == 2:
        print("{} argument:".format(argu))
    elif length == 1:
        print("{} arguments.".format(argu))
    elif length > 1:
        print("{} arguments:".format(argu))
    while i < length:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1


if __name__ == "__main__":
    argument_count()
