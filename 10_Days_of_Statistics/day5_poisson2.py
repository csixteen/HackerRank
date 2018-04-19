X, Y = map(float, input().split(" "))
A = 160 + 40*(X + X**2)
B = 128 + 40*(Y + Y**2)

print(round(A, 3))
print(round(B, 3))
