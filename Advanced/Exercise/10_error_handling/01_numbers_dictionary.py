def fill_dictionary():
    numbers_dictionary = {}

    while True:
        key = input()
        if key == 'Search':
            break
        value = input()
        if value == 'Search':
            break
        try:
            number = int(value)
            numbers_dictionary[key] = number
        except Exception:
            print("The variable number must be an integer")

    return numbers_dictionary


def find_in_store(store):
    searched = input()

    while searched != "Remove":
        print(numbers_dictionary.get(searched, "Number does not exist in dictionary"))
        searched = input()


def remove_from_store(numbers_dictionary):
    line = input()
    while line != "End":
        searched = line
        try:
            del numbers_dictionary[searched]
        except Exception:
            print('Number does not exist in dictionary')
            line = input()
            continue

        line = input()


numbers_dictionary = fill_dictionary()
find_in_store(numbers_dictionary)
remove_from_store(numbers_dictionary)
print(numbers_dictionary)