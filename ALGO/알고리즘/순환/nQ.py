def queen(level):
    global count
    if level == n:
        count += 1
        return
    else:
        for i in range(n):
            col[level] = i
            if is_promising(level):
                queen(level+1)

def is_promising(level):
    for i in range(level):
        if col[i] == col[level] or abs(col[i] - col[level]) == abs(level-i):
            return False
    return True


n = int(input())
col = [0] * n

count = 0
queen(0)
print(count)