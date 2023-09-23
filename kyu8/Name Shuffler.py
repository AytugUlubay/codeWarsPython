"""Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

"john McClane" --> "McClane john"
"""
def name_shuffler(str_):
    l= str_.split(" ")
    return " ".join((l[::-1]))
