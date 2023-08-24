"""This is a question from codingbat

Given an integer n greater than or equal to 0, create and return an array with the following pattern:

squareUp(3) => [0, 0, 1, 0, 2, 1, 3, 2, 1]
squareUp(2) => [0, 1, 2, 1]
squareUp(4) => [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]
n<=1000."""
def square_up(n):
    l=[]
    for i in range(n,0,-1):
        for j in range(1,i+1):
            l.append(j)
        for k in range(n-j):
            l.append(0)
    return l[::-1]
