"""Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise."""
def is_digit(n):
    if n.isdigit() and int(n)>9:
        return False
    return n.isdigit()
