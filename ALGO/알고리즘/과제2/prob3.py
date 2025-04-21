import random
import time

n = 100000
m = 100000

arr = []

for i in range(n):
  arr.append(random.randint(0,n))

start_time = time.time()

for i in range(m):
  if (random.randint(0,1) == 0): # 삽입
    arr.append(random.randint(0,n))
  else: # 최대값 삭제
    max_num = max(arr)
    for j in range(len(arr)):
      if max_num == arr[j]:
        arr[j], arr[len(arr)-1] = arr[len(arr)-1], arr[j]
        arr.pop()
        break

end_time = time.time()

executed_time = end_time - start_time
minutes, seconds = divmod(executed_time, 60)
print(f"배열 총시간: {int(minutes)}분 {float(seconds)}초")