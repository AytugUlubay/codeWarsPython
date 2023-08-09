"""For any given linear sequence, calculate the function [f(x)] and return it as a string.

Assumptions for this kata are:

the sequence argument will always contain 5 values equal to f(0) - f(4).
the function will always be in the format "nx +/- m", "x +/- m", "nx', "x" or "m"
if a non-linear sequence simply return "Non-linear sequence" or Nothing in Haskell.
Examples (input -> output):
[0, 1, 2, 3, 4]   -> "f(x) = x"
[0, 3, 6, 9, 12]  -> "f(x) = 3x"
[1, 4, 7, 10, 13] -> "f(x) = 3x + 1"
[0, 0, 1, 1, 1]   -> "Non-linear sequence"
"""
def get_function(sequence):
    l=list(sequence)
    for i in range(len(l)-2):
        if l[i+1]-l[i]!=l[i+2]-l[i+1]:
            return ("Non-linear sequence")
    a=l[1]-l[0]
    b=l[0]
    print(l[0])
    if a==1:
        if b==0:
            return "f(x) = x"
        if b<0:
            return "f(x) = x - {}".format(-b)
        return "f(x) = x + {}".format(b)
    if a==-1:
        return "f(x) = -x + {}".format(b)
    if a==0:
        return "f(x) = {}".format(b)
    if b==0:
        return "f(x) = {}x".format(a)
    if b<0:
        return "f(x) = {}x - {}".format(a, -b)
    return "f(x) = {}x + {}".format(a, b)
