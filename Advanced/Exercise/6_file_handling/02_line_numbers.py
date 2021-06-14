with open('02_input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

out = []
for index, line in enumerate(lines):
    letter_count = sum([len(word) for word in line.split()])
    punctuation_count = sum([1 for word in line.split() for letter in word if letter in r'-,\.!?\''])

    out.append(f'Line {index + 1}: {line} ({letter_count - punctuation_count})({punctuation_count})')

with open('02_output.txt', 'w') as out_file:
    out_file.writelines([line + '\n' for line in out])
