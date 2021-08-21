from collections import deque

working_bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
symbols = [s for s in input().split()]

total_honey = 0

while working_bees and nectar:
    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()
    if len(symbols) == 0:
        break
    elif len(working_bees) == 0:
        break

    if last_nectar >= first_bee:
        symbol = symbols[0]
        if symbol == "+":
            total_honey += abs(first_bee + last_nectar)
            symbols.remove(symbol)
        elif symbol == "-":
            total_honey += abs(first_bee - last_nectar)
            symbols.remove(symbol)
        elif symbol == "*":
            total_honey += abs(first_bee * last_nectar)
            symbols.remove(symbol)
        elif symbol == "/":
            total_honey += abs(first_bee / last_nectar)

            symbols.remove(symbol)

    else:
        working_bees.appendleft(first_bee)


print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {(', '.join(map(str, working_bees)))}")
if nectar:
    print(f"Nectar left: {(', '.join(map(str, nectar)))}")