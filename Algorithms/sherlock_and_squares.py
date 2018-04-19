import math

for _ in range(int(input())):
    a, b = map(int, input().split(" "))
    print(math.floor(b**0.5) - math.ceil(a**0.5) + 1)
