#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    result = 0
    for index in range(1, argc + 1):
        result += int(argv[index])
    print("{:d}".format(result))
