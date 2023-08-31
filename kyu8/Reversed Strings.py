"""Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
"""
def solution(string):
    l=list(string)
    k=l[::-1]
    return "".join(k)
