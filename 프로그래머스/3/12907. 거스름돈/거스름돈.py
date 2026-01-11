def solution(n, money):
    answer = 0
    DPTable = [0] * (n+1)
    DPTable[0] = 1
    for coin in money:
        for price in range(coin, n + 1):
            DPTable[price] += DPTable[price - coin]
    answer = DPTable[n] % 1000000007
    return answer