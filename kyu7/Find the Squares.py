"""Problem
Complete the function that takes an odd integer (0 < n < 1000000) which is the difference between two consecutive perfect squares, and return these squares as a string in the format "bigger-smaller"

Examples
9  -->  "25-16"
5  -->  "9-4"
7  -->  "16-9"  """
def find_squares(num):
    x=int((num+1)/2)
    y=num-x
    res="-".join([str(x**2),str(y**2)])
    return res
