"""Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!"""
def remove_every_other(my_list):
    l2=[]
    for i in range (0,len(my_list)):
        if i%2==0:
            l2.append(my_list[i])
    return(l2)
