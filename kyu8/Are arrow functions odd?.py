"""Time to test your basic knowledge in functions! Return the odds from a list:

[1, 2, 3, 4, 5]  -->  [1, 3, 5]
[2, 4, 6]        -->  []"""
def odds(l): 
    k = [i for i in l if i % 2 == 1]
    return k 
