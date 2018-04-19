n = int(input())
array = list(map(int, input().split(" ")))
k, i = array[-1], n-1
while i > 0:
    if array[i-1] > k:
        array[i] = array[i-1]
        print(" ".join(map(str, array)))
        i -= 1
    else:
        array[i] = k
        print(" ".join(map(str, array)))
        break
else:
    if i == 0:
        array[i] = k
        print(" ".join(map(str, array)))
