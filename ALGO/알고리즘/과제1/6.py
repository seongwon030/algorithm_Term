n = int(input())
sequence = list(map(int, input().split()))

def isReached(cur, visited):
    if cur >= len(sequence) - 1:
        print("Yes")
        return True

    if sequence[cur] == 0 or visited[cur]:
        return False

    visited[cur] = True

    for i in range(1, sequence[cur] + 1):
        if isReached(cur + i, visited):
            return True
    return False

visited = [False] * n
if not isReached(0, visited):
    print("No")