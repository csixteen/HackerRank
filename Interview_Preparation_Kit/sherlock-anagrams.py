from array import array


def isAnagram(a, b):
    N = len(a)
    arr_a = array('i', [0]*26)
    arr_b = array('i', [0]*26)
    for i in range(N):
        arr_a[ord(a[i]) - ord('a')] += 1
        arr_b[ord(b[i]) - ord('a')] += 1

    for i in range(26):
        if arr_a[i] != arr_b[i]:
            return False
    return True

def countAnagrams(a, b):
    len_a, len_b = len(a), len(b)
    j= total= 0
    while j <= len_b - len_a:
        if isAnagram(a, b[j:j+len_a]):
            total += 1
        j += 1
    return total

def countAllAnagrams(a, stop, b):
    total = 0
    while stop < len(a) and len(a[:stop]) <= len(b):
        total += countAnagrams(a[:stop], b)
        stop += 1
    return total

def sherlockAndAnagrams(s):
    total = 0
    N = len(s)
    for i in range(N-1):
        total += countAllAnagrams(s[i:], 1, s[i+1:])
    return total

if __name__ == '__main__':
    print(sherlockAndAnagrams('ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel'))
