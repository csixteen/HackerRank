def array_manipulation(n, queries):
    x= max_= 0
    arr = [0]*n
    for a, b, k in queries:
        arr[a-1] += k
        if b < n:
            arr[b] -= k

    for i in arr:
        x += i
        if max_ < x:
            max_ = x

    return max_

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    queries = [list(map(int, input().rstrip().split())) for _ in range(m)]
    result = array_manipulation(n, queries)
    print(result)
