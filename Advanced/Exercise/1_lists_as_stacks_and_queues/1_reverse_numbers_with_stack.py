number = input().split()
stack = []

for i in range(len(number)):
    stack.append(number.pop())

print(' '.join(stack))
