def fib_sum(n):
    sum, a, b = 0, 1, 1
    c = a + b
    while c < n:
        sum += c
        a = b + c
        b = c + a
        c = a + b

    return sum

n = int(input())
for i in range(n):
    print(fib_sum(int(input())))
