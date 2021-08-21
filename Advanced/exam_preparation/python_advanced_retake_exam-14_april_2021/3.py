def flights(*args):
    dictionary = {}
    for n in range(0, len(args), 2):
        if args[n] == 'Finish':
            return dictionary
        elif args[n] not in dictionary:
            dictionary[args[n]] = int(args[n+1])
        else:
            dictionary[args[n]] += int(args[n+1])


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
