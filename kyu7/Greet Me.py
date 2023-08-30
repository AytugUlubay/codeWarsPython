""" DESCRIPTION:
Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation point.

Example:

"riley" --> "Hello Riley!"
"JACK"  --> "Hello Jack!"
"""
def greet(name): 
    l=(x.lower() for x in list(name))  #first i will change name to list and all  letter's lowercase
    k=[]
    for i,e in enumerate(l):
        if i==0:
            k.append(e.upper())
        else:
            k.append(e)
    s="".join(k)
    return f"Hello {s}!"
