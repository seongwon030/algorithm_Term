def hanoi(n, start, temp, dest):
    if n == 1:
        print(start, dest)
    else:
        hanoi(n-1, start, dest, temp)
        print(start, dest)
        hanoi(n-1, temp, start, dest)

n = int(input())
if n <= 20:
    print(2**n -1)
    hanoi(n, 1,2,3)
