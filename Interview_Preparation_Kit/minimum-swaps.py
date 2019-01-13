def minimum_swaps(arr):
    N = len(arr)
    i= swaps= 0
    while i < N:
        while arr[i] != i+1:
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            swaps += 1
        i += 1

    return swaps

if __name__ == '__main__':
    print(minimum_swaps([2, 3, 4, 1, 5]))

