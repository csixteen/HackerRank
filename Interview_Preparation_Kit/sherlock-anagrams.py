from collections import Counter


def isAnagram(a, b):
    return Counter(a) == Counter(b)

def countAnagrams(a, b):
    len_a, len_b = len(a), len(b)
    if len_a > len_b:
        return 0
    count = 1 if isAnagram(a, b[:len_a]) else 0
    return count + countAnagrams(a, b[1:])

def countAllAnagrams(a, stop, b):
    if stop == len(a) or len(a[:stop]) > len(b):
        return 0
    else:
        return countAnagrams(a[:stop], b) + countAllAnagrams(a, stop+1, b)

def sherlockAndAnagrams(s):
    total = 0
    N = len(s)
    for i in range(N-1):
        total += countAllAnagrams(s[i:], 1, s[i+1:])
    return total

if __name__ == '__main__':
    print(sherlockAndAnagrams('ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel'))
