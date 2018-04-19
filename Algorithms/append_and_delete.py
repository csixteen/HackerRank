s, t, k = input(), input(), int(input())
len_s, len_t = len(s), len(t)

if s == t and ((not k % 2) or (k > 2*len_s)):
    print("Yes")
else:
    i = 0
    while i < min(len_t, len_s) and s[i] == t[i]:
        i += 1

    num_diff = len_s + len_t - 2*i
    if any([
        num_diff <= k and num_diff % 2 and k % 2,
        num_diff <= k and not num_diff % 2 and not k % 2,
        k >= 2*len_t
    ]):
        print("Yes")
    else:
        print("No")
