from collections import Counter

s = input()
d = dict(Counter(s))
odd = 0
for char, count in d.items():
    if count % 2:
        odd += 1
        if odd > 1:
            print("NO")
            break
else:
    print("YES")
