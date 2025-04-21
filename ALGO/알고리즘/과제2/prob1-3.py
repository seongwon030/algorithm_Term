## 합병정렬
import time

def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2

  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  return merge(left, right)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i+=1
    else:
      result.append(right[j])
      j+=1

  result.extend(left[i:])
  result.extend(right[j:])

  return result


filename = "harry_full.txt"

start_time = time.time()

with open(filename, "r", encoding="utf-8") as file:
    text = file.read()
    words = text.split()

words = merge_sort(words)

end_time = time.time()
elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)
print(f"합병정렬 시간: {int(minutes)}분 {float(seconds)}초")