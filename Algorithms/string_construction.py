n = int(input().strip())
for i in range(n):
    s = input().strip()
    s_list = list(set(s))
    print(len([1 for c in s_list if s_list.count(c)]))
