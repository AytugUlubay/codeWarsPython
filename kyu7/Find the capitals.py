""" DESCRIPTION:
Instructions
Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

Example (Input --> Output)
"CodEWaRs" --> [0,3,4,6] """
def capitals(word):
    #i will change word to list
    l=list(word)
    k=[]
    print(l)
    #i'm controling capital letters
    for i in range(len(l)):
        if l[i].isupper():
            k.append(i)
    return k
