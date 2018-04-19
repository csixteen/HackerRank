def mean(a, l):
    return sum(a) / l

def std_deviation(a, l):
    m = mean(a, l)
    return (sum([(i - m)**2 for i in array]) / l)**0.5

n = int(input())
array = list(map(int, input().split(" ")))
print(std_deviation(array, n))
