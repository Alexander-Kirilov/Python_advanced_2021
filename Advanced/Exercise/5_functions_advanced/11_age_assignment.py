def age_assignment(*names, **ages):
    result = {name: 0 for name in names}

    for first_letter, age in ages.items():
        for name in result:
            if name.startswith(first_letter):
                result[name] = age
    return result

