from itertools import combinations

def is_valid(s):
    if len(set(s)) == 1:
        return False

    t = s[:2] * (len(s) // 2)
    if len(s) % 2:
        t += s[0]
    return t == s

len_s = int(input())
s = input()
if len_s == 1:
    print(0)
elif is_valid(s):
    print(len_s)
else:
    max_len, letters = 0, list(set(s))
    if len(letters) == 1:
        print(0)
    else:
        for p in combinations(letters, len(letters)-2):
            t = s
            for r in p:
                t = t.replace(r, "")
            if is_valid(t) and len(t) > max_len:
                max_len = len(t)
        print(max_len)
