def gcd(a, b):
    if a < b:
        a, b = b, a
    if (a % b) == 0:
        return b
    else:
        return gcd(b, a % b)

def compact_gcd(a,b):
    if b == 0:
        return a
    else:
        return compact_gcd(b, a % b)

# print(gcd(12,15))
# print(compact_gcd(12,15))

# 최대값 찾기
def find_max(n, arr):
    if (n == 1):
        return arr[0]
    else:
        return max(arr[n-1], find_max(n-1, arr))

# print(find_max(5, [1,2,3,4,5]))

def printInBinary(n):
    if (n < 2):
        print(n)
    else:
        printInBinary(n//2)
        print(n%2)

# print(printInBinary(10))

# 정수들 정렬되어 있을 떄 두  배열의 정수들이 서로소인지
def isDisjoint(m, A, n, B):
    if (m <= 0 or n <= 0):
        return True
    elif (A[m-1] == B[n-1]):
        return False
    elif (A[m-1] > B[n-1]):
        return isDisjoint(m-1, A, n, B)
    else:
        return isDisjoint(m, A, n-1, B)


# 이진탐색 반복문
def binarySearch(data, n, target):
    begin, end = 0, n-1
    while begin <= end:
        mid = (begin + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            begin = mid + 1
        else:
            end = mid - 1
    return -1

# 이진탐색 재귀
def binarySearch2(data, target, begin, end):
    if (begin > end):
        return -1
    else:
        mid = (begin + end) // 2
        if (data[mid] == target):
            return mid
        elif (data[mid] < target):
            return binarySearch2(data, target, mid+1, end)
        else:
            return binarySearch2(data, target, begin, mid-1)

# 배열 data에 합이 k가 되는 쌍이 존재하는지 검사.
# n개의 정수가 오름차순으로 정렬되어 있음.
def twoSum(data, n, k):
    begin, end = 0, n-1
    while begin < end:
        if (data[begin] + data[end] == k):
            return True
        elif (data[begin] + data[end] < k):
            begin += 1
        else:
            end -= 1
    return False

# print(twoSum([1,2,3,4,5], 5, 15))

