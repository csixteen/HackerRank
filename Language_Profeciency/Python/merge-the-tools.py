def clean(string):
    chars = set()
    res = []
    for c in string:
        if c not in chars:
            res.append(c)
            chars.add(c)
    return "".join(res)

def merge_the_tools(string, k):
    for i in range(len(string) // k):
        print(clean(string[i*k:(i+1)*k]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

