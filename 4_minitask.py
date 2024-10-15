def create_reverse_dict(d):
    reverse_dict = {}
    for key, value in d.items():
        if not isinstance(value, (int, float, str, bool, tuple)):
            raise TypeError(
                f"Значение {value} не может быть использовано в качестве ключа, так как оно не является хешируемым.")

        if value in reverse_dict:
            existing_value = reverse_dict[value]
            if isinstance(existing_value, tuple):
                reverse_dict[value] = existing_value + (key,)
            else:
                reverse_dict[value] = (existing_value, key)
        else:
            reverse_dict[value] = key

    return reverse_dict

d = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}
try:
    reversed_d = create_reverse_dict(d)
    print(reversed_d)
except TypeError as e:
    print(e)