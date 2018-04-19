t = int(input())
for i in range(t):
    n, k = map(int, input().split(" "))
    array = list(map(int, input().split(" ")))
    print("YES" if len(list(filter(lambda x: x <= 0, array))) < k else "NO")
