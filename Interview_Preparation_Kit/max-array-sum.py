from array import array

def maxSubsetSum(arr):
    if len(arr) == 1:
        return arr[0]

    global_max = max(arr[:2])
    if len(arr) < 3:
        return global_max

    local_max = array('i', [-(10**4)] * len(arr))
    local_max[0] = arr[0]
    local_max[1] = global_max
    for i in range(2, len(arr)):
        local_ = max(arr[i], global_max, local_max[i-2] + arr[i])
        local_max[i] = local_
        global_max = max(local_, global_max)

    return global_max


if __name__ == '__main__':
    input()
    arr = list(map(int, input().split()))
    print(maxSubsetSum(arr))
