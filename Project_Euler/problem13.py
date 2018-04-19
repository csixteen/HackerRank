n = int(input())
res = 0
for i in range(n):
    res += int((input().strip())[:25])

print(str(res)[:10])
