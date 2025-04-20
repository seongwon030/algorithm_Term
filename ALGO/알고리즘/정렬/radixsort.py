from collections import deque

def radixSort():
  nums = list(map(int, input().split()))
  buckets = [deque() for _ in range(10)]

  max_val = max(nums)
  queue = deque(nums)
  digit = 1

  while (max_val >= digit):
    while queue:
      num = queue.popleft()
      buckets[(num // digit) % 10].append(num)

    for bucket in buckets:
      while bucket:
        queue.append(bucket.popleft())
    print(digit, "의 자릿수 정렬", list(queue))
    digit *= 10
  
  print(list(queue))

radixSort()