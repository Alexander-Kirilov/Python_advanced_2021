def read_matrix(n):
    matrix = [[x for x in input().split(" ")] for r in range(n)]
    return matrix


def is_valid_bound(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


n = int(input())
matrix = read_matrix(n)

player_position = []
for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == "A":
            player_position.append(r)
            player_position.append(c)
            matrix[r][c] = "*"

row = player_position[0]
col = player_position[1]

collected_tea = 0

while collected_tea < 10:
    command = input()
    previous_row = row
    previous_col = col

    if command == "up":
        row -= 1
        if row not in range(0, len(matrix)) or col not in range(0, len(matrix)) or matrix[row][col] == "R":
            matrix[row][col] = "*"

            break

    elif command == "down":
        row += 1
        if row not in range(0, len(matrix)) or col not in range(0, len(matrix)) or matrix[row][col] == "R":
            matrix[row][col] = "*"

            break

    elif command == "left":
        col -= 1
        if row not in range(0, len(matrix)) or col not in range(0, len(matrix)) or matrix[row][col] == "R":
            matrix[row][col] = "*"

            break

    elif command == "right":
        col += 1
        if row not in range(0, len(matrix)) or col not in range(0, len(matrix)) or matrix[row][col] == "R":
            matrix[row][col] = "*"

            break

    if matrix[row][col].isdigit():
        collected_tea += int(matrix[row][col])

    matrix[row][col] = "*"

if collected_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
print(*[" ".join(x) for x in matrix], sep="\n")
