from operator import itemgetter

def mean(a, l):
    return sum(a) / l

def median(a, l):
    a = sorted(a)
    if not l % 2:
        return (a[(l//2) - 1] + a[l//2]) / 2
    else:
        return a[l//2]

def mode(a):
    d = dict.fromkeys(a)
    for k in d.keys():
        d[k] = a.count(k)

    sorted_d = sorted(d.items(), key=itemgetter(1, 0))
    m = max(sorted(list(set(d.values()))))
    list_of_values = list(d.values())
    return sorted_d[-list_of_values.count(m)][0]

l = int(input())
array = list(map(int, input().split(" ")))

print(mean(array, l))
print(median(array, l))
print(mode(array))
