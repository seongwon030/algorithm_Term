arr = [2,5,3,0,2,3,0,3]

def counting_sort(arr):
  if not arr:
    return []
  
  max_val = max(arr)

  count = [0] * (max_val+1)
  
  # 각 숫자의 개수 세기
  for num in arr:
    count[num] += 1

  # 누적합 배열로 변환
  for i in range(1, len(count)):
    count[i] += count[i-1]

  # 정렬된 배열 생성
  result = [0] * len(arr)
  for num in reversed(arr):
    count[num] -= 1
    result[count[num]] = num

  return result

print(counting_sort(arr))