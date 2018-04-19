t = int(input())
for i in range(t):
    n = int(input())
    print(len([1 for x in map(int, list(str(n))) if x != 0 and not n % int(x)]))
