n = int(input())
zeros = 0
while n > 1:
    if n & 1 == 0:
        zeros += 1
    n >>= 1
print(2**zeros)
