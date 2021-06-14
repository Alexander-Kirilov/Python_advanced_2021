def age_assignment(*names, **ages):
    result = {name: 0 for name in names}

    for first_letter, age in ages.items():
        for name in result:


            if name.startswith(first_letter):
                result[name] = age
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))