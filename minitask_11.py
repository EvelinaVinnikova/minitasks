def cycle(iterable):
    while True:
        yield from iterable


def chain(*iterables):
    for iterable in iterables:
        yield from iterable


def take(iterable, n):
    for i, element in enumerate(iterable):
        if i >= n:
            break
        yield element


# Example usage:
print(list(take(cycle([1, 2, 3]), 10)))

my_list = ['H', 1, 2, "Hannah", "Soda", "Time"]
chained = chain(my_list, [1, 2, 3])
print(list(chained))
