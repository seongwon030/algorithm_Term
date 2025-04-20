def search_matrix(matrix, target):
    m,n = len(matrix), len(matrix[0])
    i,j = 0, n-1

    while i< m and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1

    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(search_matrix(matrix, target))