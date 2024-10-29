def flatten_with_depth(list_1, depth=None):
    new_list = []
    for i in list_1:
        if isinstance(i, list) and (depth is None or depth > 0):
            new_list.extend(flatten_with_depth(i, depth - 1 if depth is not None else None))
        else:
            new_list.append(i)
    return new_list

list_test = flatten_with_depth([1, 2, [4, 5], [6, [7]], 8])
assert list_test == [1,2,4,5,6,7,8], print("Assert error\n")

list_test = (flatten_with_depth([1, 2, [4, 5], [6, [7]], 8], depth = 1))
assert list_test == [1,2,4,5,6,[7],8], print("Assert error\n")

list_test = (flatten_with_depth([1, 2, [4, 'a'], [6, [7]], 8, ['abc', 'a']], depth = 1))
assert list_test == [1,2,4,'a',6,[7],8,'abc','a'], print("Assert error\n")

list_test = (flatten_with_depth([1, 2, [4, 'a'], [[6, [7]], 8], ['abc', ['a']]], depth = 2))
assert list_test == [1,2,4,'a',6,[7],8,'abc','a'], print("Assert error\n")