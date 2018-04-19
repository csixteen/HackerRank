a = tuple(map(int, input().split(" ")))
b = tuple(map(int, input().split(" ")))

alice, bob = 0, 0
for ai, bi in zip(a, b):
    if ai > bi:
        alice += 1
    elif bi > ai:
        bob += 1

print(alice, bob, sep=' ')
