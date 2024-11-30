def cycle(iterable):
    saved = []
    for element in iterable:
        saved.append(element)
    yield saved
    while saved:
        for element in saved:
            yield element

def chain(*iterables):
    result = []
    for obj in iterables:
        for element in obj:
            result.append(element)
    return result

for i, item in enumerate(cycle([1,2,3])):
    print(item)
    if i > 10:
        break

my_list = ['H', 1, 2, "Hannah", "Soda", "Time"]
a = chain(my_list, [1,2,3])
print(a)
for i in a:
    print(i)

