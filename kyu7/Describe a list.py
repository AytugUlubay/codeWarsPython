""" DESCRIPTION:
Write function describeList which returns "empty" if the list is empty or "singleton" if it contains only one element or "longer"" if more."""
def describeList(list):
    if len(list)==0:
        return("empty")
    elif len(list)==1:
        return("singleton")
    else: return("longer")
