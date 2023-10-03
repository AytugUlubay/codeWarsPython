"""Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in th same order.

"h,o,l,a"
"""
def print_array(arr):
    s=""
    for i,e in enumerate(arr):
        if i==0:
            s=str(e)
        else:
            s = s+ "," + str(e)
    return s
