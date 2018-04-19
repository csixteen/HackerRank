def nextMove(r, c, grid, p):
    if r != p[0]:
        return "UP" if r > p[0] else "DOWN"
    else:
        return "LEFT" if c > p[1] else "RIGHT"

n = int(input())
r,c = map(int, input().split(" "))
grid = []
for i in range(n):
    row = input().strip()
    grid.append(row)
    if row.count("p"):
        p = (i, row.index("p"))

print(nextMove(r, c, grid, p))
