def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr if x[0] < pivot[0] or (x[0] == pivot[0] and x[1] < pivot[1])]
    middle = [x for x in arr if x[0] == pivot[0] and x[1] == pivot[1]]
    right = [x for x in arr if x[0] > pivot[0] or (x[0] == pivot[0] and x[1] > pivot[1])]

    return quick_sort(left) + middle + quick_sort(right)


arr = [[5,9], [-2,3], [5,7], [8,3], [0,3], [-2,7]]
print(quick_sort(arr))
