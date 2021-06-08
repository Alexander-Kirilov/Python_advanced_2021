def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return not is_even(num)


def even_odd(*args):
    command = args[len(args)-1]

    numbers = args[0:-1]

    if command == "even":
        return list(filter(is_even, numbers))
    elif command == "odd":
        return list(filter(is_odd, numbers))
