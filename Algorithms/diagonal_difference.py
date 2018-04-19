n = int(input())
matrix = [list(map(int, input().split(" "))) for _ in range(n)]
print(abs(sum([row[i] for i, row in enumerate(matrix)]) - sum([list(reversed(row))[i] for i, row in enumerate(matrix)])))
