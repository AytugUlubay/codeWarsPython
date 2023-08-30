""" DESCRIPTION:
Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'
"""
def remove_duplicate_words(s):
    l=s.split(" ") # i will split words by space
    k=[]
    for i in l:
        if i not in k:
            k.append(i)
    m=" ".join(k)
    return m
