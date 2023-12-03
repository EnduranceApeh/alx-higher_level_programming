#!/usr/bin/python3
a = 10
b = 80
tmp = a
a, b = b, tmp
print("a={:d} - b={:d}".format(a, b))
