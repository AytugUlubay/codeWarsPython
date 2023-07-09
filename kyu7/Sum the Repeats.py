"""Write a function that takes a list comprised of other lists of integers and returns the sum of all numbers that appear in two or more lists in the input list. Now that might have sounded confusing, it isn't:

repeat_sum([[1, 2, 3],[2, 8, 9],[7, 123, 8]])
>>> sum of [2, 8]
return 10

repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]])
>>> sum of []
return 0

repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]])
sum of [1,8]
return 9"""
def repeat_sum(l):
    k = []
    for i in range(len(l)):
        for j in l[i]:
            m = i + 1
            while m < len(l):
                if j in l[m]:
                    k.append(j)
                    break
                m += 1
    s=set(k)
    x=list(s)
    return(sum(x))
