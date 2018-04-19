n = int(input())
x = list(map(int, input().split(" ")))
w = list(map(int, input().split(" ")))
print(round(sum([number * weight for number, weight in zip(x, w)]) / sum(w), 1))
