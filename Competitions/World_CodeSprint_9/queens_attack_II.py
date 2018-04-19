n, o = map(int, input().split())
r, c = map(int, input().split())
total_squares = (n - 1) * 2  # Vertical and Horizontal

# Positive diagonal
if c >= r:
    total_squares += c - r + n - 1
elif c < r:
    total_squares += n - r + c - 1

# Negative diagonal
if r + c - 1 <= n:
    total_squares += r + c - 2
elif r + c - 1 > n:
    total_squares += 2*n - r - c

# We now check for obstables
for i in range(o):
    ri, ci = map(int, input().split())
    # Horizontal intersection
    if ri == r:
        if ci < c:
            total_squares -= ci
        else:
            total_squares -= n - ci + 1
    # Vertical intersection
    elif ci == c:
        if ri < r:
            total_squares -= ri
        else:
            total_squares -= n - ri + 1
    # Positive Diagonal
    elif (ci - c) / (ri - r) == 1:
        if ri > r:
            total_squares -= min(r - c + n - ri + 1, n - ri + 1)
        else:
            total_squares -= min(ri, ri - c + r + 1)
    # Negative Diagonal
    elif (ci - c) / (ri - r) == -1:
        if ri > r:
            total_squares -= min(n - ri + 1, r + c - ri)
        else:
            total_squares -= min(r + c - ci, n - ci + 1)

print(total_squares)
