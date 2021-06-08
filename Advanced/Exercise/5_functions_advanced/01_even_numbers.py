def is_even(n):
    return n % 2 == 0


numbers = [int(n) for n in input().split()]
print(list(filter(is_even, numbers)))
