n, k, q = map(int, input().split(" "))
array = list(map(int, input().split(" ")))
for _ in range(q):
    print(array[(int(input())-k) % n])
