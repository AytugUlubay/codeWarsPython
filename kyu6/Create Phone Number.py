"""Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses! """
def number(x):
    number_str = ''.join(str(num) for num in x)
    return int(number_str)

def create_phone_number(n):
    k = n[:3]
    l = n[3:6]
    m = n[6:]
    k1 = number(k)
    l1 = number(l)
    m1 = number(m)
    return f"({k1:03}) {l1:03}-{m1:04}"
