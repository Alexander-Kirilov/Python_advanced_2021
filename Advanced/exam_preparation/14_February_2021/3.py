from collections import deque


def stock_availability(inventory, command, *args):
    inventory_list = deque(inventory)

    if command == 'delivery':
        inventory_list.extend(args)
    elif command == 'sell':
        if args:
            if isinstance(args[0], int):
                for element in range(args[0]):
                    inventory_list.popleft()
            else:
                inventory_list = [x for x in inventory_list if x not in args]
        else:
            inventory_list.popleft()

    return list(inventory_list)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie", 'ivab', 'banana'))