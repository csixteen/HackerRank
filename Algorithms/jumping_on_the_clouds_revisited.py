n, k = map(int, input().split(" "))
clouds = input().split(" ")
print(100 - 2*len([1 for i in range(0, n, k) if clouds[i] == '1']) - n//k)
