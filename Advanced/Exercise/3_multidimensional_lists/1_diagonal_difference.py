def read_matrix(rows):
    matrix = []

    for _ in range(rows):
        matrix.append([])
        for elem in input().split():
            inner_list = matrix[-1]
            inner_list.append(int(elem))

    return matrix


n = int(input())
matrix = read_matrix(n)

result_1 = 0
result_2 = 0

for i in range(n):
    result_1 += matrix[i][i]

for i in range(n):
    result_2 += matrix[len(matrix) - 1 - i][i]

print(abs(result_1 - result_2))