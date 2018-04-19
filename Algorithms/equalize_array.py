from collections import Counter

n, A = int(input()), list(map(int, input().split(" ")))
print(n - Counter(A).most_common(1)[0][1])
