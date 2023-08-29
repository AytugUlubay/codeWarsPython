"""DESCRIPTION:
An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK" 
"""
def is_anagram(test, original):
    l = [x.lower() for x in list(test)]
    k = [y.lower() for y in list(original)]
    l2=l.copy()
    if len(l)!=len(k):
        return False
    else:
        for i in l :
            if i not in k:
                return False
            l2.remove(i)
            k.remove(i)
        if len(k)==0 and len(l2)==0:
            return True
        return False
