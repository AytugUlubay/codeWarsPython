"""Write a function that doubles every second integer in a list, starting from the left.

Example:

For input array/list :

[1,2,3,4]
the function should return :

[1,4,3,8]"""
def double_every_other(lst):
    l=[]
    for i in range(len(lst)):
        if i%2==0:
            l.append(lst[i])
        else:
            l.append(2*lst[i])
    return(l)
