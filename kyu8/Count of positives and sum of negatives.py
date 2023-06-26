"""Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65]."""
def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return([])
    else :
      s1= 0
      s2= 0
      for i in range(0,len(arr)) :
        if arr[i]> 0:
            s1 = s1 + 1
        elif arr[i] < 0:
            s2 = s2 + arr[i]
      return([s1,s2])
