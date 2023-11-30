#!/usr/bin/python3
from sys import argv
arguements = argv[1:]
if __name__ == "__main__":
    if (len(arguements) > 1):
        print(f"{len(arguements)} arguments: ")
    elif (len(arguements) == 0):
        print(f"{len(arguements)} arguments. ")
    else:
        print(f"{len(arguements)} argument: ")
    # iterate through the arguement and print by index starting from index 1
    length = len(arguements)
    for index in range(length):
        arg = 1 + index
        print(f"{arg}: {arguements[index]}")
