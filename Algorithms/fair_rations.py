def fair_rations(b, n):
    if len(b) == 2 and (not b[0] % 2) and (not b[1] % 2):
        return 0
    elif len(b) == 2 and (b[0] % 2) and (b[1] % 2):
        return 2

    odds = [i for i in range(len(b)) if b[i] % 2]
    l_odds = len(odds)
    if l_odds > n or l_odds % 2:
        return "NO"
    elif l_odds == 0:
        return 0
    else:
        s = 0
        for i in range(0, l_odds, 2):
            s += (odds[i+1]-odds[i]) * 2
        return s

n = int(input())
b = list(map(int, input().split(" ")))
print(fair_rations(b, n))
