heroes = input().split(', ')

inventory = {hero: {} for hero in heroes}

line = input()
while line != "End":
    hero, item_name, item_cost = line.split('-')

    if item_name not in inventory[hero]:
        inventory[hero][item_name] = int(item_cost)

    line = input()

# for hero in heroes:
#     cost = sum(inventory[hero].values())
#     item_count = len(inventory[hero])
#     print(f'{hero} -> Item: {item_count}, Cost: {cost}')

print('\n'.join(f'{hero} -> Items: {len(inventory[hero])}, Cost: {sum(inventory[hero].values())}' for hero in heroes))
