n, k = map(int, input().split(" "))
total = [tuple(map(int, input().split(" "))) for i in range(n)]
i = sorted([x[0] for x in total if x[1] == 1])
print(sum([e[0] for e in total]) - 2*sum(i[:len(i)-k])*int(len(i) > k))
