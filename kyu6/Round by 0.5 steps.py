"""Round any given number to the closest 0.5 step

I.E.

solution(4.2) = 4
solution(4.3) = 4.5
solution(4.6) = 4.5
solution(4.8) = 5
Round up if number is as close to previous and next 0.5 steps.

solution(4.75) == 5 """
def solution(n):
    m=int(n)
    x=n-m
    if x<0.25:
        return m
    elif 0.25<=x<0.75:
        return m+ 0.5
    return m+1
