from collections import deque

tasks = [int(el) for el in input().split(", ")]

searched_index = int(input())
result = 0
cycle = deque(sorted([(tasks[index], index) for index in range(len(tasks))]))

while cycle:
    number, index = cycle.popleft()
    result += number
    if index == searched_index:
        break

print(result)

# input
# 3, 1, 10, 1, 2
# 0
