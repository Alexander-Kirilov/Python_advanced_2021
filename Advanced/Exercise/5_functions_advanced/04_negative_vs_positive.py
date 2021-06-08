numbers = [int(x) for x in input().split()]

positive = filter(lambda num: num >= 0, numbers)
negative = filter(lambda num: num <= 0, numbers)

sum_pos = sum(positive)
sum_negat = sum(negative)

print(sum_negat)
print(sum_pos)

if sum_pos > abs(sum_negat):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")