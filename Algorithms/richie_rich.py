def get_parts(number, n):
    if n % 2:
        return number[:n//2], number[n//2], number [n//2 + 1:]
    else:
        return number[:n//2], None, number[n//2:]

def difference(left, right):
    return len([1 for x, y in zip(left, reversed(right)) if x != y])

def largest(number, n, k):
    if n == 1 and k > 0:
        return '9'

    left, middle, right = get_parts(number, n)
    diffs = difference(left, right)
    if diffs > k:
        return -1

    new_part = []
    for x, y in zip(left, reversed(right)):
        if x == y:
            if (x != '9' or y != '9') and k-2 >= diffs:
                new_part.append('9')
                k -= 2
            else:
                new_part.append(x)
        elif x != y and (x == '9' or y == '9'):
            new_part.append('9')
            k -= 1
            diffs -= 1
        elif x != y and (k-2 >= diffs-1):
            new_part.append('9')
            k -= 2
            diffs -= 1
        else:
            new_part.append(max(x, y))
            k -= 1
            diffs -= 1

    if k > 0 and middle is not None:
        middle = '9'

    return "{}{}{}".format(
        "".join(new_part), 
        middle or "", 
        "".join(reversed(new_part))
    )

n, k = list(map(int, input().strip().split(' ')))
number = input().strip()
print(largest(number, n, k))
