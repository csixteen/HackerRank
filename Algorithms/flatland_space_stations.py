n, m = map(int, input().split(" "))
stations = sorted(list(map(int, input().split(" "))))
maximum = 0
if stations[0] != 0:
    maximum = stations[0]
if stations[-1] != n-1:
    maximum = max(maximum, n - 1 - stations[-1])
for i in range(m-1):
    maximum = max(maximum, (stations[i+1] - stations[i]) // 2)
print(maximum)
