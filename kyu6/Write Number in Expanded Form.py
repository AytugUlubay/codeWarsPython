"""You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0."""
def expanded_form(num):
    k=[]
    i=1
    if num<10:
        return('{}'.format(num))
    else:
        while num//10>=1:
            a=num%(10**i)
            if a != 0:
                k.append(a)
            num=num-a
            i+=1
        l=k[::-1]
        return(" + ".join(str(x) for x in l))
