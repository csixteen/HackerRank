a = input()
b = input()
set_a = set(a)
set_b = set(b)
total = sum([a.count(i)+b.count(i) for i in list(set_a ^ set_b)]) \
        + sum([abs(a.count(i)-b.count(i)) for i in list(set_a & set_b)])
print(total)
