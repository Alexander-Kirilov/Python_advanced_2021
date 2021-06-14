from collections import deque


def print_what_left():
    if len(firework_effects) > 0:
        print(f"Firework Effects left: {', '.join([str(el) for el in firework_effects])}")
    if len(explosive_power) > 0:
        print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")
    print(f"Palm Fireworks: {palm_firework}")
    print(f"Willow Fireworks: {willow_firework}")
    print(f"Crossette Fireworks: {crossette_firework}")


firework_effects = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ") if el != '0']

palm_firework = 0
willow_firework = 0
crossette_firework = 0
is_success = False


while firework_effects:
    first_firework = firework_effects.popleft()
    last_explosive = explosive_power.pop()
    if first_firework <= 0:
        explosive_power.append(last_explosive)
        continue
    elif last_explosive <= 0:
        firework_effects.appendleft(first_firework)
        if len(explosive_power) <= 0:
            is_success = False
            break
        continue

    explosive_mix = first_firework + last_explosive

    if explosive_mix % 3 == 0 and explosive_mix % 5 != 0:
        palm_firework += 1
    elif explosive_mix % 5 == 0 and explosive_mix % 3 != 0:
        willow_firework += 1
    elif explosive_mix % 5 == 0 and explosive_mix % 3 == 0:
        crossette_firework += 1
    else:
        first_firework -= 1
        firework_effects.append(first_firework)
        explosive_power.append(last_explosive)

    if palm_firework and willow_firework and crossette_firework >= 3:
        is_success = True
        break
    if len(explosive_power) <= 0:
        is_success = False
        break

if is_success:
    print("Congrats! You made the perfect firework show!")
    print_what_left()
else:
    print("Sorry. You can't make the perfect firework show.")
    print_what_left()
