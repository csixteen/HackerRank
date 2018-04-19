n, m = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
num = 0
for i in range(max(A), min(B)+1):
    if len([1 for ai in A if not i % ai]) != n:
        continue

    if len([1 for bi in B if not bi % i]) != m:
        continue

    num += 1

print(num)
