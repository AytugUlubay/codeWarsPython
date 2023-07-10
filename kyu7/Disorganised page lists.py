"""You're given an ancient book that unfortunately has a few pages in the wrong position, fortunately your computer has a list of every page number in order from 1 to n.

You're supplied with an array of numbers, and should return an array with each page number that is out of place. Incorrect page numbers may appear next to each other. Duplicate incorrect page numbers are possible.

Example:

Given: list = [1,2,10,3,4,5,8,6,7]
Return: [10,8]
Your returning list should have the incorrect page numbers in the order they were found."""
def find_page_number(pages):
    i=0
    k=[]
    while i<len(pages):
        if i+1!=pages[i]:
            k.append(pages[i])
            pages.remove(pages[i])
            i-=1
        i+=1
    return(k)
