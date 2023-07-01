"""Define a function that removes duplicates from an array of numbers and returns it as a result.

The order of the sequence has to stay the same."""
def distinct(seq):
    result = []
    for i in range(len(seq)):
        if seq[i] not in result:
            result.append(seq[i])
    return(result)
