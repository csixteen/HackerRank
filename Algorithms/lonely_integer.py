from collections import Counter
from operator import itemgetter

_, A = input(), list(map(int, input().split(" ")))
print(sorted([(x, y) for x, y in Counter(A).items()], key=itemgetter(1))[0][0])
