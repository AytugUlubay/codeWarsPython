"""Given a string, turn each character into its ASCII character code and join them together to create a number - let's call this number total1:

'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667
Then replace any incidence of the number 7 with the number 1, and call this number 'total2':

total1 = 656667
              ^
total2 = 656661
              ^
Then return the difference between the sum of the digits in total1 and total2:"""
def calc(x):
    l=list(x)
    k=[]
    for i in range(len(l)):
        k.append(ord(l[i]))
    m=0
    for j in k:
        if '7' in str(j):
            m+= 1
    return(m*6)
