sequences = input().split('|')

numbers = [
    [el for el in seq.split()]
    for seq in sequences
]
numbers.reverse()

numbers = [number for sequence in numbers for number in sequence]

print(' '.join(numbers))
