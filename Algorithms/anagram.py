from collections import Counter

def changes(s1, s2):
    c1, c2 = Counter(s1), Counter(s2)
    n = 0
    for c in c2:
        current = c2[c] - c1.get(c, 0)
        if current > 0:
            n += current
    return n

for _ in range(int(input())):
    s = input()
    l = len(s)
    if l % 2:
        print(-1)
    else:
        print(changes(s[:l//2], s[l//2:]))
