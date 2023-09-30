"""Complete the function which converts a binary number (given as a string) to a decimal number."""
def bin_to_decimal(inp):
    n=len(inp)-1
    total=0
    for i in inp:
        total += int(i) * (2**n)
        n -= 1
    return total
