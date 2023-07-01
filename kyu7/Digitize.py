"""Given a non-negative integer, return an array / a list of the individual digits in order.

Examples:

123 => [1,2,3]

1 => [1]

8675309 => [8,6,7,5,3,0,9]"""
def digitize(n):
    if n==0:
        return([0])
    else:
        a=[]
        while n>0:
            a.insert(0,n%10)
            n= n//10
        return(a)
