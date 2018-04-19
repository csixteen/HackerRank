n, k = map(int, input().split(" "))
houses = list(map(int, input().split(" ")))
# Get the min and max in one go (O(n))
min_x, max_x = 100000, 0
for h in houses:
    if h < min_x:
        min_x = h
    if h > max_x:
        max_x = h

# Populate the X axis in one go (O(n))
x_axis = [None] * ((max_x - min_x) + 1)
for h in houses:
    x_axis[h - min_x] = False

# Add radio transmitters
counter, i = 0, 0
while i < len(x_axis):
    if x_axis[i] == False:
        if i < len(x_axis) <= i + k:
            x_axis[i] = True
            counter += 1
            i = i + k + 1
        else:
            j = k
            while  j < len(x_axis) and j >= 0:
                if x_axis[i + j] == False:
                    x_axis[i + j] = True
                    counter += 1
                    i = i + j + k + 1
                    break
                else:
                    j -= 1
    else:
        i += 1

print(counter)
