def median(a, l):
    if not l % 2:
        return int((a[l//2-1] + a[l//2]) / 2)
    else:
        return int(a[l//2])

n = int(input())
array = list(sorted(map(int, input().split(" "))))

if not n % 2:
    left, middle, right = array[:n//2], None, array[n//2:]
else:
    left, middle, right = array[:n//2], array[n//2], array[(n//2)+1:]

print(median(left, len(left)))
print(middle or median(array, n))
print(median(right, len(right)))
