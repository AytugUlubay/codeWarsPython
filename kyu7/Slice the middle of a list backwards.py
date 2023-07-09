"""Write a function that takes a list of at least four elements as an argument and returns a list of the middle two or three elements in reverse order."""
def reverse_middle(lst):
    n=len(lst)
    if n%2==1:
        start=int((n+1)/2)
        stop=int((n-3)/2)-1
        return(lst[start:stop:-1])
    else:
        start=int(n/2)
        stop=int(n/2-1)-1
        return(lst[start:stop:-1])
