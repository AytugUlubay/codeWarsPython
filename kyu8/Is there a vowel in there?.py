"""Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

If they are, change the array value to a string of that vowel.

Return the resulting array."""
def is_vow(inp):
    print(inp)
    vowels = [97,101,105,111,117]
    l=[]
    for i in inp:
        if i in vowels:
            l.append(chr(i))
        else :
            l.append(i)
    return l
