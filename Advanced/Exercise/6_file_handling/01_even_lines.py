import re
file = open('01_input.txt')

for index, line in enumerate(file.readlines()):
    if index % 2 != 0:
        continue

    line = re.sub(r'[-,.!?]', '@', line)
    line = ' '.join(reversed(line.split()))

    print(line.strip())

file.close()
