_, scores = input(), list(map(int, input().split()))
_max = _min = scores[0]
_cmax = _cmin = 0
for score in scores:
    if score < _min:
        _cmin += 1
        _min = score
    elif score > _max:
        _cmax += 1
        _max = score

print(_cmax, _cmin)
