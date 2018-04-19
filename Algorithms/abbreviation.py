def abbreviation(a, b, len_a, len_b):
    if len_b > len_a:
        return "NO"

    if a == b:
        return "YES"

    if (len_a > len_b) and a.isupper():
        return "NO"

    aux = [x for x in a if x.isupper()]
    if len(aux) > len_b:
        return "NO"

    aux = "".join(aux)
    if aux == b:
        return "YES"

    f = a.find(b)
    if f != -1:
        aux = a[:f] + a[f+len_b:]
        if aux.islower():
            return "YES"
        else:
            return "NO"

    i, j = 0, 0
    while j < len_b and i < len_a:
        if a[i].isupper() and a[i] != b[j]:
            return "NO"
        elif a[i].upper() == b[j]:
            j += 1
            i += 1
        else:
            while (i < len_a) and (a[i].upper() != b[j]):
                i += 1

    if i >= len_a and j < len_b:
        return "NO"
    else:
        return "YES"


q = int(input())
for i in range(q):
    a, b = input(), input()
    print(abbreviation(a, b, len(a), len(b)))
