n = int(input())
a = sorted(list(map(int, input().split(" "))))
while len(a) > 0:
    print(len(a))
    a = sorted(list(filter(lambda x: x > 0, map(lambda x: x - a[0], a))))
