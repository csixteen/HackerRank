num, den = map(int, input().split(" "))
n = int(input())
p = num / den
print(round(((1-p)**(n-1))*p, 3))
