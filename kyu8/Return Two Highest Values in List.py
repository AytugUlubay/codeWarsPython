"""In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

The result should also be ordered from highest to lowest.

Examples:

[4, 10, 10, 9]  =>  [10, 9]
[1, 1, 1]  =>  [1]
[]  =>  []"""
def two_highest(arg1):
    if len(arg1)==0:
        return([])
    else :
        l= sorted(arg1)
        l2 = l[::-1]
        m1=l2[0]
        m2= None
        i=0
        if l2.count(m1)!=len(l2):
            while m1==l2[i]:
                i+=1
                if i >= len(l2):
                    break
            if i < len(l2):
                m2 = l2[i]
        if m2 is None:
            return([m1])
        else:
            return([m1, m2])
