def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def p(k, l):
    e = 2.71828
    return (l**k)*(e**-l) / fact(k)

l = float(input())
k = int(input())
print(round(p(k, l), 3))
