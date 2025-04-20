# N개의 정수가 저장된 배열에서 연속된 수를 합하여 얻을 수 있는 최대값

# O(n3)
max_sum = 0
arr = [1,2,3,4,5]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        sum = 0
        for k in range(i, j+1):
            sum += arr[k]
        if (sum > max_sum):
            max_sum = sum

print(max_sum)

# O(n2)
max_sum = 0
arr = [1,2,3,4,5]
for i in range(len(arr)):
    sum = 0
    for j in range(i, len(arr)):
        sum += arr[j]
        if (sum > max_sum):
            max_sum = sum

print(max_sum)

# O(n)
max_sum = 0
arr = [1,2,3,4,5]

max_so_far = 0
max_here = 0
for i in range(len(arr)):
    max_here = max(max_here + arr[i], 0)
    if (max_here > max_so_far):
        max_so_far = max_here
print(max_so_far)