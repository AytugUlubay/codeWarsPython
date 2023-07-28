"""Given a positive integer N, return the largest integer k such that 3^k < N.

For example,

largest_power(3) == 0
largest_power(4) == 1
You may assume that the input to your function is always a positive integer."""
def largest_power(N):
    if N==1:
        return(-1)
    else:
        i=1
        while 3**i<N:
            i+=1
        return(i-1)
