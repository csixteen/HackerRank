def happy_bugs(b, n):
    # Only underscores: they are happy
    if b.count("_") == n:
        return "YES"

    if len(b) == 1:
        return "NO"

    if b.count("_") > 0:
        b = sorted(b)
    for i in range(n):
        if (i == 0) and (b[i] != "_") and(b[i] != b[i+1]):
            return "NO"
        if (i == n-1) and (b[i] != "_") and (b[i] != b[i-1]):
            return "NO"
        if (0 < i < n-1) and (b[i] != b[i-1]) and (b[i] != b[i+1]):
            return "NO"
    return "YES"


g = int(input())
for i in range(g):
    n, b = int(input()), input()
    print(happy_bugs(b, n))
