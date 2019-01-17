from collections import defaultdict

def whatFlavors(cost, money):
    cost_map = defaultdict(list)
    for i, c in enumerate(cost):
        cost_map[c].insert(0, i)

    for c, positions in cost_map.items():
        if money-c == c and len(positions) > 1:
            print(min(positions)+1, max(positions)+1)
            return
        elif money-c == c and len(positions) <= 1:
            continue
        elif (money-c) in cost_map:
            ids = [positions[0]+1, min(cost_map[money-c])+1]
            print(min(ids), max(ids))
            return


if __name__ == '__main__':
    for _ in range(int(input())):
        money = int(input())
        input()
        cost = list(map(int, input().split()))
        whatFlavors(cost, money)

