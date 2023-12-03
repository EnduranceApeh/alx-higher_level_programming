#!/usr/bin/python3
a, b = 10, 80
tmp = a
a, b = b, tmp
print("a={:d} - b={:d}".format(a, b))
