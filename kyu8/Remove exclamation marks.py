"""Write function RemoveExclamationMarks which removes all exclamation marks from a given string."""
def remove_exclamation_marks(s):
    l=""
    for i in s:
        if i != "!":
            l= l + i
    return l
