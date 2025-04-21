## 힙정렬
import time

def heapify(arr, index, heap_size):
  largest = index
  left = 2 * index + 1
  right = 2 * index +2

  if left < heap_size and arr[left] > arr[largest]:
    largest = left

  if right < heap_size and arr[right] > arr[largest]:
    largest = right

  if largest != index:
    arr[largest], arr[index] = arr[index], arr[largest]
    heapify(arr, largest, heap_size)

def heap_sort(arr):
  n = len(arr)

  for i in range(n//2 -1, -1, -1):
    heapify(arr, i, n)

  for i in range(n-1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, 0, i)

  return arr

filename = "harry_full.txt"

start_time = time.time()

with open(filename, "r", encoding="utf-8") as file:
    text = file.read()
    words = text.split()

heap_sort(words)

end_time = time.time()
elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)
print(f"힙정렬: {int(minutes)}분 {float(seconds)}초")