"""Write function replaceAll (Python: replace_all) that will replace all occurrences of an item with another.

Python / JavaScript: The function has to work for strings and lists.

Example: replaceAll [1,2,2] 1 2 -> in list [1,2,2] we replace 1 with 2 to get new list [2,2,2]

replaceAll(replaceAll(array: [1,2,2], old: 1, new: 2) // [2,2,2]"""
def replace_all(obj, find, replace):
    if type(obj) == list:
        for i in range(len(obj)):
            if find == obj[i]:
                obj[i] = replace
        return obj
    else:
        l = list(obj)
        for i in range(len(l)):
            if find == l[i]:
                l[i] = replace
        s = "".join(str(x) for x in l)
        return s
