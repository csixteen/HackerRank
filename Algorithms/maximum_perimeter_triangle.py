def is_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def find_max(a):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and i != k and j != k and is_triangle(a[i], a[j], a[k]):
                    return " ".join(map(str, sorted([a[i], a[j], a[k]])))
    return -1

n = int(input())
sticks = list(map(int, input().split(" ")))
sticks.sort(reverse=True)
print(find_max(sticks))
