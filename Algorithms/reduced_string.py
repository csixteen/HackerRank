import re

s = input()
while re.search(r"(\w)(\1)", s):
    s = re.sub(r"(\w)(\1)", "", s)

print(s or "Empty String")
