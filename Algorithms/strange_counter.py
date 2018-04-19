t, n = int(input()), 0
while True:
    base_t = 3*(2**(n-1)) - 2
    if base_t > t:
        break
    n += 1

print(6*(2**(n-2)) - t - 2)
