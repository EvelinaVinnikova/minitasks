def pair_lists(list1, list2):
    min_length = min(len(list1), len(list2))
    result = []
    for i in range(min_length):
        result.append((list1[i], list2[i]))

    return result

list1 = input().split()
list2 = input().split()
print(pair_lists(list1, list2))
list1 = [1, 2, 3]
list2 = ["a", "b"]
list3 = [(1, 'a'), (2, 'b')]
assert pair_lists(list1, list2) == list3, "assert_error"
list1 = ["a 3","b 2" ,"c 1" ]
list2 = ["a", "b"]
list3 = [("a 3", "a"), ("b 2", "b")]
assert pair_lists(list1, list2) == list3, "assert_error"
list1 = [" ", "-", ")"]
list2 = ["a", "b", "c"]
list3 = [(" ", "a"), ("-", "b"), (")", "c")]
assert pair_lists(list1, list2) == list3, "assert_error"
list1 = [-1, 0 ,-9, -1]
list2 = ["/", "-", "+"]
list3 = [(-1, '/'), (0, '-'), (-9, '+')]
assert pair_lists(list1, list2) == list3, "assert_error"