""" DESCRIPTION:
Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com? """
def remove_url_anchor(url):
    # i will change url to list
    l=list(url)
    #i will look for # then i delete rest
    for i in range(len(l)):
        if l[i] =="#":
            break
    if "#"not in l :
            return url
    k=l[:i]
    s="".join(k)
    return s
