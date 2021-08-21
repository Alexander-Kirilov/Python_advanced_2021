from collections import deque

working_bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
symbols = deque([s for s in input().split()])

total_honey = 0

while working_bees and nectar:
    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()

    if last_nectar >= first_bee:
        symbol = symbols.popleft
        if symbol == "+":
            total_honey += abs(first_bee + last_nectar)
            break
        elif symbol == "-":
            total_honey += abs(first_bee - last_nectar)
            break
        elif symbol == "*":
            total_honey += abs(first_bee * last_nectar)
            break
        elif symbol == "/":
            total_honey += abs(first_bee / last_nectar)
            break

    else:
        working_bees.appendleft(first_bee)

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {(', '.join(map(str, working_bees)))}")
if nectar:
    print(f"Nectar left: {(', '.join(map(str, nectar)))}")
