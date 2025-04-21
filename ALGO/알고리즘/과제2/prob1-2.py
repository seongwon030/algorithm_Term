## 삽입정렬
import time

def insert(arr):
  for i in range(1,len(arr)):
    for j in range(i, 0, -1):
      if arr[j] < arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
      else:
        break

filename = "harry_full.txt"

start_time = time.time()

with open(filename, "r", encoding="utf-8") as file:
    text = file.read()
    words = text.split()

insert(words)

end_time = time.time()
elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)
print(f"총 실행 시간: {int(minutes)}분 {float(seconds)}초")