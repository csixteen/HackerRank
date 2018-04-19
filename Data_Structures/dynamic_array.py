N, Q = map(int, input().split())
last_ans, seq_list = 0, [[] for _ in range(N)]
for _ in range(Q):
    o, x, y = map(int, input().split())
    if o == 1:
        seq_list[(x^last_ans) % N].append(y)
    else:
        seq = seq_list[(x^last_ans) % N]
        last_ans = seq[y % len(seq)]
        print(last_ans)
