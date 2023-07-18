"""DESCRIPTION:
Implement a function, multiples(m, n), which returns an array of the first m multiples of the real number n. Assume that m is a positive integer.

Ex.

multiples(3, 5.0)
should return

[5.0, 10.0, 15.0]"""
def multiples(m, n):
    l = []
    for i in range(1, m+1):
        l.append(n * i)
    return l
