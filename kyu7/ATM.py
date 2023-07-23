"""An ATM has banknotes of nominal values 10, 20, 50, 100, 200 and 500 dollars. You can consider that there is a large enough supply of each of these banknotes.

You have to write the ATM's function that determines the minimal number of banknotes needed to honor a withdrawal of n dollars, with 1 <= n <= 1500.

Return that number, or -1 if it is impossible."""
def solve(n):
    if n % 10 != 0:
        return -1
    else:
        k = []
        m = n
        if m // 500 > 0:
            k.append(m // 500)
            m = m - (m // 500) * 500
        if m // 200 > 0:
            k.append(m // 200)
            m = m - (m // 200) * 200
        if m // 100 > 0:
            k.append(m // 100)
            m = m - (m // 100) * 100
        if m // 50 > 0:
            k.append(m // 50)
            m = m - (m // 50) * 50
        if m // 20 > 0:
            k.append(m // 20)
            m = m - (m // 20) * 20
        k.append(m // 10)
    return sum(k)
