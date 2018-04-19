class Chapter:
    def __init__(self, t, k, previous_last_page):
        self.t = t
        self.ppc = 1*int(t % k != 0) + t//k
        self.initial_page = previous_last_page + 1
        self.last_page = previous_last_page + self.ppc

    def get_special(self):
        s, array = 0, list(range(1, self.t+1))
        for p in range(self.initial_page, self.last_page+1):
            if p in array[:k]:
                s += 1
            del array[:k]
        return s

n, k = map(int, input().split(" "))
t = list(map(int, input().split(" ")))
special, plp = 0, 0
for c in range(n):
    chap = Chapter(t[c], k, plp)
    plp = chap.last_page
    special += chap.get_special()

print(special)
