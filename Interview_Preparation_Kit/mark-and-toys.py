def maximumToys(prices, k):
    total= count= 0
    for p in prices:
        total += p
        if total > k:
            break
        count += 1
    return count



if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    print(maximumToys(sorted(prices), k))

