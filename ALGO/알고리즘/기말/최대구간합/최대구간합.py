def max_sum_interval(A):
    max_ends_at = A[0]
    max_sum = A[0]

    max_List = []

    for i in range(1,len(A)):
        max_ends_at = max(max_ends_at + A[i], A[i])
        if max_ends_at > max_sum:
            max_List.append(A[i])
            max_sum = max_ends_at

    return max_List, max_sum

max_List,max_sum = max_sum_interval([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(max_sum)
print(max_List)