"""Given a number return the closest number to it that is divisible by 10.

Example input:

22
25
37
Expected output:

20
30
40"""
def closest_multiple_10(i):
    if i%10<5:
        return((i//10)*10)
    else:
        return(((i//10)+1)*10)
