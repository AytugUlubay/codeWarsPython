"""Implement function which will return sum of roots of a quadratic equation rounded to 2 decimal places, if there are any possible roots, else return None/null/nil/nothing. If you use discriminant,when discriminant = 0, x1 = x2 = root => return sum of both roots. There will always be valid arguments.

Quadratic equation - https://en.wikipedia.org/wiki/Quadratic_equation"""
def roots(a,b,c):
    delta=b**2-4*a*c
    if delta>=0:
        return round(-b/a,2)
    return None
