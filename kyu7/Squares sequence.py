"""DESCRIPTION:
Complete the function that returns an array of length n, starting with the given number x and the squares of the previous number. If n is negative or zero, return an empty array/list.

Examples
2, 5  -->  [2, 4, 16, 256, 65536]
3, 3  -->  [3, 9, 81]"""
def squares(x, n):
    l=[x]
    sqr=x
    if n<1:
        return([])
    else:
        while len(l)<n:
            sqr=sqr**2
            l.append(sqr)
    return(l)
