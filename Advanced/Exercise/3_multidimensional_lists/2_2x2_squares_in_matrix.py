def read_matrix(rows):
    matrix = []
    for _ in range(rows):
        chars = input().split()
        matrix.append(chars)

    return matrix


num_rows, num_cols = input().split()
num_rows, num_cols = int(num_rows), int(num_cols)
matrix = read_matrix(num_rows)

count_of_2x2_matrix = 0

for i in range(num_rows - 1):
    for j in range(num_cols - 1):
        if matrix[i][j] == matrix[i+1][j] and matrix[i][j] == matrix[i+1][j+1] and matrix[i][j] == matrix[i][j+1]:
            count_of_2x2_matrix += 1

print(count_of_2x2_matrix)
