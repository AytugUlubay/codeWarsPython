"""Have a look at the following numbers.

 n | score
---+-------
 1 |  50
 2 |  150
 3 |  300
 4 |  500
 5 |  750
Can you find a pattern in it? If so, then write a function getScore(n)/get_score(n)/GetScore(n) which returns the score for any positive number n.

Note Real test cases consists of 100 random cases where 1 <= n <= 10000"""
def get_score(n):
    score = 50
    for i in range(2, n + 1):
        score += 50 * i
    return score
