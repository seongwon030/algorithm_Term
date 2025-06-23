def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr if x < pivot]
    mid =  [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)

print(quick_sort([1, 3, 2, 4, 5]))

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
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

print(merge_sort([1, 3, 2, 4, 5]))

def bubble_sort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j+1]

    return arr

print(bubble_sort([1, 3, 2, 4, 5]))

# 삽입 정렬: 현재 원소를 앞쪽 정렬된 부분에 삽입
def insertion_sort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

    return arr

print(insertion_sort([1, 3, 2, 4, 5]))

# 선택 정렬 : 가장 작은 값을 선택해 앞으로 보냄
def selection_sort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr

print(selection_sort([1, 3, 2, 4, 5]))

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

