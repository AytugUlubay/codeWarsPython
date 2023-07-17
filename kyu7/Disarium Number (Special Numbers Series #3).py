"""DESCRIPTION:
Definition
Disarium number is the number that The sum of its digits powered with their respective positions is equal to the number itself.

"""
def disarium_number(number):
    l=list(str(number))
    total=0
    for i in range(len(l)):
        total+=int(l[i])**(i+1)
    if total==number:
        return("Disarium !!")
    else: return("Not !!")
