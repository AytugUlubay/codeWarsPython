""" DESCRIPTION:
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!""" 
def capitalize(s):
    l=list(s)
    k=[]
    m=[]
    for i,e in enumerate(l):
        if i%2==0:
            k.append(e.upper())
            m.append(e)
        else:
            m.append(e.upper())
            k.append(e)
    x= "".join(k)
    y= "".join(m)
    return [x,y]
