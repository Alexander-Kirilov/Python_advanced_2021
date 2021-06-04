n, m = input().split()
n, m = int(n), int(int(m))

set_a, set_b = set(), set()

for _ in range(n):
    set_a.add(input())

for _ in range(m):
    set_b.add(input())

present_in_both = set_a.intersection(set_b)

for element in present_in_both:
    print(element)
