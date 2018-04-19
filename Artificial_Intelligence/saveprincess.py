def displayPathToPrincess(b, p, grid):
    vertical = [(lambda x, y: "UP" if x < y else "DOWN")(p[0], b[0]) for x in range(abs(p[0]-b[0]))]
    horizontal = [(lambda x, y: "LEFT" if x < y else "RIGHT")(p[1], b[1]) for x in range(abs(p[1]-b[1]))]
    print("\n".join(vertical))
    print("\n".join(horizontal))

m = int(input())
grid = []
for i in range(m):
    row = input().strip()
    grid.append(row)
    if row.count('p'):
        p = (i, row.index('p'))

    if row.count('m'):
        b = (i, row.index('m'))

displayPathToPrincess(b, p, grid)
