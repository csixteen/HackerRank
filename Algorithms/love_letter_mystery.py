def operations(s):
    len_s, op = len(s), 0
    i, j = 0, len_s - 1
    while i <= len_s // 2 and j >= len_s // 2:
        op += abs(ord(s[i]) - ord(s[j]))
        i += 1
        j -= 1
    
    return op

t = int(input())
for _ in range(t):
    print(operations(input()))
