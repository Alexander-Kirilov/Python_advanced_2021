def get_magic_triangle(n):
    matrix = []
    for i in range(2):
        matrix.append([])
        matrix[i] += (i + 1) * [1]
    for k in range(2, n):
        matrix.append([])
        for l in range(k + 1):
            if l == 0:
                matrix[k].append(matrix[k - 1][l])
            elif 0 < l < k:
                matrix[k].append(matrix[k - 1][l - 1] + matrix[k - 1][l])
            elif l == k:
                matrix[k].append(matrix[k - 1][l - 1])
    return matrix


print(get_magic_triangle(5))
