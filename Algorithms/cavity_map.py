# First we build the map
n = int(input())
m = [list(map(int, list(input()))) for _ in range(n)]
c = [row[:] for row in m]  # To avoid comparisons with "X"

# We want to skip the borders up, down, left and right
for i in range (1, n-1):
    for j in range(1, n-1):
        if all([
            m[i][j-1] < m[i][j],
            m[i][j+1] < m[i][j],
            m[i-1][j] < m[i][j],
            m[i+1][j] < m[i][j]
        ]):
            c[i][j] = "X"

print("\n".join(["".join(map(str, row)) for row in c]))
