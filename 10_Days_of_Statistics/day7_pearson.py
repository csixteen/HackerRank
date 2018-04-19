def std_dev(x, u, n):
    return (sum([(i - u)**2 for i in x]) / n)**0.5

def r(x, y, n):
    ux = sum(x) / n
    uy = sum(y) / n
    sx = std_dev(x, ux, n)
    sy = std_dev(y, uy, n)
    return sum([(xi-ux)*(yi-uy) for xi, yi in zip(x, y)]) / (n*sx*sy)

n = int(input())
x = list(map(float, input().strip().split(" ")))
y = list(map(float, input().strip().split(" ")))
print(round(r(x, y, n), 3))
