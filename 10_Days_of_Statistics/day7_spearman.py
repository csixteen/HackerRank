def rs(x, y, n):
    return 1 - (6*sum([(xi-yi)**2 for xi, yi in zip(x,y)])/(n*(n**2 - 1)))

def get_rank(a):
    d = {e:i for i, e in enumerate(sorted(a), 1)}
    return [d[xi] for xi in a]

n = int(input())
rank_x = get_rank(list(map(float, input().strip().split(" "))))
rank_y = get_rank(list(map(float, input().strip().split(" "))))
print(round(rs(rank_x, rank_y, n), 3))
