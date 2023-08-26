""" DESCRIPTION:
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""
def reverse_words(text):
    # i will split list words by words
    l= text.split(" ")
    k=[]
    # now i will reverse words 
    for i in l:
        k.append(i[::-1])
    s= " ".join(k)
    return s
