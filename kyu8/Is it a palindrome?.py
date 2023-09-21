"""Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar."""
def is_palindrome(s):
    l=s.lower()
    for i in range(1,len(l)):
        if l[i-1]!=l[-i]:
            return False
    return True
