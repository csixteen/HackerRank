from itertools import combinations

def ncombinations(l):
    return sum([len(list(combinations(l, i))) for i in range(1,len(l))])+1

n = int(input())
x = int(input())
l = list(range(n))
p = ncombinations(l)
print(x - p if x > p else p - x)
