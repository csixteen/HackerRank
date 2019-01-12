def minion_game(s):
    vowels = 'AEIOU'
    length = len(s)
    v= c= 0

    for i in range(len(s)):
        if s[i] in vowels:
            v += length-i
        else:
            c += length-i

    if v > c:
        print('Kevin {}'.format(v))
    elif v == c:
        print('Draw')
    else:
        print('Stuart {}'.format(c))

if __name__ == '__main__':
    s = input()
    minion_game(s)
