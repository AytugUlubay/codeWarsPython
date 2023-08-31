"""Your car is old, it breaks easily. The shock absorbers are gone and you think it can handle about 15 more bumps before it dies totally.

Unfortunately for you, your drive is very bumpy! Given a string showing either flat road (_) or bumps (n). If you are able to reach home safely by encountering 15 bumps or less, return Woohoo!, otherwise return Car Dead"""
def bumps(road):
    # i will change road to list
    l=list(road)
    count=0 # numbers of bumps
    for i in l:
        if i=="n":
            count+=1 # i'm counting bumps
    if count> 15: 
        return "Car Dead"
    return "Woohoo!"
