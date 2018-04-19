n, p = int(input()), 5
total = 0
for i in range(n):
    like = p // 2
    total += like
    p = like * 3
print(total)
