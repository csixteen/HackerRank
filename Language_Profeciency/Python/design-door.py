def design(n, m):
    p = [('.|.'*(2*i-1)).center(m, '-') for i in range(1, (n-1) // 2 + 1)]
    return '\n'.join(p + ['WELCOME'.center(m, '-')] + p[::-1])

if __name__ == '__main__':
    n, m = list(map(int, input().split(' ')))
    print(design(n, m))

