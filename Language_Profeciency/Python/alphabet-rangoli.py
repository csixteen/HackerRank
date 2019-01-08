def letters(size, k):
    return '-'.join([chr(abs(i)+(ord('a')+k)) for i in range(-size+1+k, size-k)])

def rangoli(size):
    middle = letters(size, 0)
    down = [letters(size, i).center(len(middle), '-') for i in range(1, size)]
    return '\n'.join(down[::-1] + [middle] + down)

if __name__ == '__main__':
    size = int(input())
    print(rangoli(size))
