## 버블정렬
import time

def bubblesort(arr):
  n = len(arr)

  for i in range(n):
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

filename = "harry_full.txt"

start_time = time.time()

with open(filename, "r", encoding="utf-8") as file:
    text = file.read()
    words = text.split()

bubblesort(words)

end_time = time.time()
elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)
print(f"총 실행 시간: {int(minutes)}분 {float(seconds)}초")