matrix = [list(map(int, input().split())) for _ in range(6)]
max_sum = None
for i in range(4):
    for j in range(4):
        s = sum(matrix[i][j:j+3]) + matrix[i+1][j+1] + sum(matrix[i+2][j:j+3])
        if max_sum is None or s > max_sum:
            max_sum = s

print(max_sum)
