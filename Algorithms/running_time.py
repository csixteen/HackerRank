def insertion_sort(l):
    shifts = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            j -= 1
            shifts += 1
        l[j+1] = key
    
    return shifts

m = int(input())
ar = list(map(int, input().split(" ")))
print(insertion_sort(ar))
