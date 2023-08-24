"""An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false"""
def is_isogram(string):
    #first i will change string to list#
    l=list(string)
    #then i will change all letters to Upper case#
    k = [x.upper() for x in l]
    #then i will control every letter and others#
    for i in range(len(k)):
        for j in range(i+1,len(k)):
            if k[i]==k[j]:
                return False
    return True
