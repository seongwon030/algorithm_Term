def selection_sort(arr):
    for i in range(len(arr)):
        max_index = 0
        for j in range(len(arr)-i):
            if arr[max_index] < arr[j]:
                max_index = j

        arr[len(arr) -1 -i], arr[max_index] = arr[max_index], arr[len(arr) -1 -i]
    return arr

print(selection_sort([1, 3, 2, 4, 5]))

def stable_selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # 최솟값을 꺼내고
        min_value = arr[min_index]

        # min_index ~ i 까지 오른쪽으로 한 칸씩 이동
        while min_index > i:
            arr[min_index] = arr[min_index - 1]
            min_index -= 1

        # 최솟값을 i 위치에 삽입
        arr[i] = min_value

    return arr

print(selection_sort([1, 3, 2, 4, 5]))

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort([1, 3, 2, 4, 5]))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

print(insertion_sort([1, 3, 2, 4, 5]))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

print(merge_sort([1, 3, 2, 4, 5]))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([1, 3, 2, 4, 5]))

def heapify(arr, index, heap_size):
    largest = index
    left = 2*index + 1
    right = 2*index + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, largest, heap_size)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr, i, n)

    for j in range(n-1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j]
        heapify(arr, 0, j)

    return arr

print(heap_sort([1, 3, 2, 4, 5]))