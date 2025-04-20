import bisect

def solve(arr,k):
    pos = bisect.bisect_left(arr,k)
    candidates = []

    if pos > 0:
        candidates.append(arr[pos-1])
    if pos < len(arr):
        candidates.append(arr[pos])

    return min(candidates, key=lambda x: (abs(x-k), x))

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

print(solve(arr,k))