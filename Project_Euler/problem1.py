n = int(input())
for i in range(n):
    x = int(input())
    m3, m5, m15 = (x-1)//3, (x-1)//5, (x-1)//15
    print(3*(m3*(m3+1)//2) + 5*(m5*(m5+1)//2) - 15*(m15*(m15+1)//2))
