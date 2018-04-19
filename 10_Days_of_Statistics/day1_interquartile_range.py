def median(a, l):
    if not l % 2:
        return float((a[l//2-1] + a[l//2]) / 2)
    else:
        return float(a[l//2])

n = int(input())
x = list(map(int, input().split(" ")))
f = list(map(int, input().split(" ")))
s = []
for xi, fi in zip(x, f):
    s.extend([xi] * fi)

s.sort()
n = len(s)

if not n % 2:
    left, _, right = s[:n//2], None, s[n//2:]
else:
    left, _, right = s[:n//2], s[n//2], s[(n//2)+1:]

print(abs(median(right, len(right)) - median(left, len(left))))
