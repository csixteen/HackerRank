from collections import deque


def isBalanced(s):
    brackets_close = {')': '(', '}': '{', ']': '['}

    if len(s) == 1 or s[0] in brackets_close:
        return 'NO'

    stack = deque(s[0])
    for c in s[1:]:
        if c in brackets_close:
            if len(stack) > 0 and brackets_close[c] == stack[-1]:
                stack.pop()
            else:
                return 'NO'
        else:
            stack.append(c)

    return 'NO' if len(stack) > 0 else 'YES'


if __name__ == '__main__':
    for _ in range(int(input())):
        print(isBalanced(input()))

