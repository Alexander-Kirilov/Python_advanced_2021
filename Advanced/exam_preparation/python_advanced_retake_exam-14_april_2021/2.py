def hit(a):
    row = int(a[1])
    col = int(a[4])
    return matrix[row][col]


player_one, player_two = input().split(', ')
score_player_one = 501
score_player_two = 501

matrix = []

for row in range(7):
    matrix.append(input().split())

hit = hit(input())
winner = False
while winner:

    hit(input())