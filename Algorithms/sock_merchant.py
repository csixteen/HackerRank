n = int(input())
socks = input().split(" ")
print(sum([socks.count(s) // 2 for s in list(set(socks))]))
