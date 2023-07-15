"""For this kata you will have to forget how to add two numbers.

16+18=214
26+39=515
122+81=1103
It can be best explained using the following meme:
In simple terms, our method does not like the principle of carrying over numbers and just writes down every number it calculates :-)

You may assume both integers are positive integers.
"""
def add(num1, num2):
    l1 = [int(d) for d in str(num1)]
    l2 = [int(e) for e in str(num2)]
    while len(l1) != len(l2):
        if len(l1) > len(l2):
            l2.insert(0, 0)
        else:
            l1.insert(0, 0)
    l3 = []
    for i in range(len(l1)):
        l3.append(str(l1[i] + l2[i]))
    result = int(''.join(l3))
    return result
