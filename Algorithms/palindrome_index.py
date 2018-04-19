def is_palindrome(s):
    return s == s[::-1]

def char_index(s):
    if is_palindrome(s):
        return -1

    i, j = 0, len(s) - 1
    l = len(s) // 2
    while i <= l and l >= l:
        if s[i] != s[j]:
            if is_palindrome(s[:i] + s[i+1:]):
                return i
            elif is_palindrome(s[:j] + s[j+1:]):
                return j
            else:
                return -1

        i += 1
        j -= 1

    return -1

for _ in range(int(input())):
    print(char_index(input()))
