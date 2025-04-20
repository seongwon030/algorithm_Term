def queen(level):
    global count
    if n == level:
        count += 1
        return

    for i in range(n):
        cols[level] = i
        if is_promising(level):
            queen(level+1)

def is_promising(level):
    for i in range(level):
        if cols[i] == cols[level] or abs(cols[i] - cols[level]) == abs(level-i):
            return False
    return True

n = int(input())
count = 0
cols = [0] * n

queen(0)
print(count)
