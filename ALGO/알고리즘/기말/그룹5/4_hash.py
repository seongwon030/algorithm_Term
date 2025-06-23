A = list(map(str, input().split()))
n = len(A)
k = int(input())

hashmap = {}
unique_counts = []

# 초기 윈도우 설정
for i in range(k):
    if A[i] in hashmap:
        hashmap[A[i]] += 1
    else:
        hashmap[A[i]] = 1

unique_counts.append(len(hashmap))

# 슬라이딩 윈도우 적용
for i in range(k, n):
    # 윈도우 왼쪽 제거
    if hashmap[A[i - k]] == 1:
        del hashmap[A[i - k]]
    else:
        hashmap[A[i - k]] -= 1

    # 윈도우 오른쪽 추가
    if A[i] in hashmap:
        hashmap[A[i]] += 1
    else:
        hashmap[A[i]] = 1

    unique_counts.append(len(hashmap))

print(', '.join(map(str, unique_counts)))

# 시간복잡도: O(n)
# 각 요소는 해시맵에서 추가, 제거, 검색이 모두 O(1)
# 따라서 n개의 요소를 처리하는 데 O(n) 시간