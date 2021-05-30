n = int(input())

stack = []

for index in range(n):
    command = input().split()
    if command[0] == '1':
        stack.append(command[1])
    elif command[0] == '2':
        stack.pop()
    elif command[0] == '3':
        if len(stack) > 0:
            print(max(stack))
    elif command[0] == '4':
        if len(stack) > 0:
            print(min(stack))

reversed_stack = []
for _ in range(len(stack)):
    reversed_stack.append(str(stack.pop()))

print(', '.join(reversed_stack))