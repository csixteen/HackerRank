def insertion_sort(A, n):
    i = 1
    while i < n:
        temp = A[i]
        j = i
        while temp < A[j-1] and j > 0:
            A[j] = A[j-1]
            j -= 1

        A[j] = temp

        i += 1
        print(" ".join(map(str, a)))

n = int(input())
a = list(map(int, input().split(" ")))
insertion_sort(a, n)
