def primality(n):
    if n == 1:
        return 'Not prime'
    if n < 4:
        return 'Prime'
    if n % 2:
        return 'Not prime'
    x = int(n**(1/2))
    for i in range(3, x+1):
        if n % x == 0:
            return 'Not prime'

    return 'Prime'
