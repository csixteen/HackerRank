t = int(input())
for i in range(t):
    n = int(input())
    print(2**((n+int(n%2>0))//2+1) - 1 - int(n%2>0))
