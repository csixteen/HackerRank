def is_funny(string):
    data = list(zip(string, reversed(string)))
    for i in range(len(string)-1):
        if abs(ord(data[i+1][0]) - ord(data[i][0])) != \
           abs(ord(data[i+1][1]) - ord(data[i][1])):
            return "Not Funny"
        return "Funny"

N = int(input())
for i in range(N):
    print(is_funny(input()))
