""" Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9. """
def square_sum(numbers):
    l = numbers
    sum = 0
    for i in range(0, len(l)):
        sum = sum + l[i] * l[i]
    return(sum)
