"""Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F """
def abbrev_name(name):
    l=list(name)
    for i,e in enumerate(l):
        if e== " ":
            break
    k=l[i+1]
    m=l[0]
    return f"{m.upper()}.{k.upper()}"
