def stock_availability(*args):
    inventory_list = args[0]
    command = args[1]
    if command == "delivery":
        for n in range(args.index('delivery')+1, len(args)):
            inventory_list.append(args[n])
        return inventory_list
    elif command == "sell":
        if args[-1] == "sell":
            return inventory_list[1:]
        if isinstance(args[-1], int):
            n = int(args[-1])
            return inventory_list[n:]
        if isinstance(args[-1], str):
            cupcakes = args[int(args.index("sell")+1):]
            for x in cupcakes:
                inventory_list = [i for i in inventory_list if not i == x]
            return inventory_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
