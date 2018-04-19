n, clouds = int(input()), input().strip().split(" ")
i, jumps = 0, 0
while i < n-1:
    i += 2 if (i+2 < n) and clouds[i+2] == '0' else 1
    jumps += 1

print(jumps)
