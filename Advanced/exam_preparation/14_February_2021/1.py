from collections import deque


def is_in_range(dictionary):
    if all([value >= 3 for value in dictionary.values()]):
        return True
    return False


firework_effects = [int(x) for x in input().split(", ")]  # deque([5, 6, 4, 16, 11, 5, 30, 2, 3, 27])
explosive_power = [int(x) for x in input().split(", ")]  # deque([1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22])

# firework_effects = [x for x in firework_effects if x > 0]  # removing negative nums
# explosive_power = [x for x in explosive_power if x > 0]  # с Фор цикъл не става защото прескача

firework_effects = deque(firework_effects)
explosive_power = deque(explosive_power)

dict_fireworks = {
    "Palm": 0,
    "Willow": 0,
    "Crossette": 0}

while len(firework_effects) > 0 and len(explosive_power) > 0 and not is_in_range(dict_fireworks):
    first_firework = firework_effects.popleft()
    last_explosive = explosive_power.pop()
    current_sum = first_firework + last_explosive
    # managed_to_create = False <<< check is out of the  main loop
    # TODO - check inline <= 0 check
    if first_firework <= 0:
        explosive_power.append(last_explosive)
    elif last_explosive <= 0:
        firework_effects.appendleft(first_firework)
    elif current_sum % 3 == 0 and not current_sum % 5 == 0:  # Palm
        dict_fireworks['Palm'] += 1
        managed_to_create = True
    elif current_sum % 5 == 0 and not current_sum % 3 == 0:  # Willow
        dict_fireworks['Willow'] += 1
        managed_to_create = True
    elif current_sum % 3 == 0 and current_sum % 5 == 0:  # Crossette
        dict_fireworks['Crossette'] += 1
        managed_to_create = True
    # if not managed_to_create: <<< contain it in the loop with else
    else:
        first_firework -= 1
        firework_effects.append(first_firework)
        explosive_power.append(last_explosive)

if not is_in_range(dict_fireworks):
    print(f"Sorry. You can't make the perfect firework show.")
    if len(firework_effects) >= 1:
        print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
    if len(explosive_power) >= 1:
        print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
else:
    print(f"Congrats! You made the perfect firework show!")
    if len(firework_effects) >= 1:
        print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
    if len(explosive_power) >= 1:
        print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

for k, v in dict_fireworks.items():
    print(f"{k} Fireworks: {v}")
