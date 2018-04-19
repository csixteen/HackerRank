def rot(i, k):
    d = 65 if i.isupper() else 97
    return chr(((ord(i) - d + k) % 26) + d)

n, s, k = int(input()), input(), int(input())
print("".join([(lambda x: rot(x, k) if x.isalpha() else x)(i) for i in s]))
