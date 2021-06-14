from functools import reduce


def flights(*args):
    return lambda x, y: x + y, {args}


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
