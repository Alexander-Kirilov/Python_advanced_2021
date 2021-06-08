command = input()
numbers = [int(x) for x in input().split()]

if command == "Even":
    filtered = filter(lambda num: num % 2 == 0, numbers)
elif command == "Odd":
    filtered = filter(lambda num: num % 2 != 0, numbers)

result = sum(filtered) * len(numbers)
print(result)