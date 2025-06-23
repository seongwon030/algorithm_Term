A = list(map(int, input().split()))
n = len(A)

k = int(input())

for i in range(n-k+1):
    B = A[i:i+k]
    print(len(set(B)), end=', ')

# 매번 슬라이싱, 중복 제거를 위해 set
# O(n*k)