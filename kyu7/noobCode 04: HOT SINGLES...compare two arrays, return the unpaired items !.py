"""Write a function that takes two arguments, and returns a new array populated with the elements that only appear once, in either one array or the other, taken only once; display order should follow what appears in arr1 first, then arr2:

hot_singles([1, 2, 3, 3], [3, 2, 1, 4, 5]) # [4, 5]
hot_singles(["tartar", "blanket", "cinnamon"], ["cinnamon", "blanket", "domino"]) # ["tartar", "domino"]
hot_singles([77, "ciao"], [78, 42, "ciao"]) # [77, 78, 42]
hot_singles([1, 2, 3, 3], [3, 2, 1, 4, 5, 4]) # [4,5]"""
def hot_singles(arr1, arr2):
    arr11=arr1.copy()
    arr22=arr2.copy()
    for i in arr1:
        if i in arr2:
            while i in arr22:
                arr22.remove(i)
            while i in arr11:
                arr11.remove(i)
    k=arr11+arr22
    s = []
    for j in k:
        if j not in s:
            s.append(j)
    return(s)
