def find_u(s):
    weights = {c: i+1 for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')} 
    subs = {}
    prev_index = 0
    for i in range(len(s)):
        if i > 0 and s[i] == s[i-1]:
            subs[s[prev_index:i+1]] = subs[s[prev_index:i]] + weights[s[i]]
        else:
            prev_index = i
            subs[s[i]] = weights[s[i]]

    return set(subs.values())

s = input()
u = find_u(s)
for _ in range(int(input())):
    if int(input()) in u:
        print('Yes')
    else:
        print('No')
