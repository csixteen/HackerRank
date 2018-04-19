heights = list(map(int, input().split(" ")))
word = input()
print(max([heights[ord(l)-97] for l in word]) * len(word))
