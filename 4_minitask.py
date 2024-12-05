def create_reverse_dict(d):
    reverse_dict = {}
    for key, value in d.items():
        if value in reverse_dict:
            exist_value = reverse_dict[value] if isinstance(reverse_dict[value], tuple) else (reverse_dict[value],)
            reverse_dict[value] = exist_value + (key,)
        else:
            reverse_dict[value] = (key,) if isinstance(key, tuple) else key
    return reverse_dict

d = {("Petrov",): 123, "Kuznezov": 123}
reversed_d = create_reverse_dict(d)
assert reversed_d == {123: (('Petrov',), 'Kuznezov')}
print(reversed_d)

input_dict = {"Ivanov": 97832, "Petrov": 55521, ("Kuznecov",): 97832}
reversed_d = create_reverse_dict(input_dict)
assert reversed_d == {97832: ('Ivanov', ('Kuznecov',)), 55521: 'Petrov'}
print(reversed_d)

input_dict = {"Alice": 42, "Bob": 42, "Charlie": 123}
reversed_d = create_reverse_dict(input_dict)
assert reversed_d == {42: ('Alice', 'Bob'), 123: 'Charlie'}
print(reversed_d)
