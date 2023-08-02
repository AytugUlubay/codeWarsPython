"""You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers, and return the result in %.

Example:

compare(13,14)=50%;
compare(23,22)=50%;
compare(15,51)=100%;
compare(12,34)=0%. """
from collections import Counter

def compare(a, b):
    l = Counter(str(a))  
    k = Counter(str(b))  
    common_chars = l & k  
    total_common_count = sum(common_chars.values())  
    per = total_common_count * 50  
    return f"{per}%"
