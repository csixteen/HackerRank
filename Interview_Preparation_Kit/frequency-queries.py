from collections import Counter


def freqQueries(queries):
    numbers = Counter()
    freqs = Counter()

    result = []
    for op, val in queries:
        if op == 1:
            freqs[numbers[val]] -= 1
            numbers[val] += 1
            freqs[numbers[val]] += 1
        elif op == 2:
            if numbers[val] > 0:
                freqs[numbers[val]] -= 1
                numbers[val] -= 1
                freqs[numbers[val]] += 1
        else:
            if freqs[val] > 0:
                result.append(1)
            else:
                result.append(0)

    return result


if __name__ == '__main__':
    queries = []
    for _ in range(int(input())):
        queries.append(list(map(int, input().split())))

    answer = freqQueries(queries)
    print('\n'.join(map(str, answer)))

