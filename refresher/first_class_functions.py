def search(sequence, target, search_method):
    for i in sequence:
        if search_method(i) == target:
            return f'Yes, \"{i["name"]}\" is found in provided sequence'
    raise RuntimeError(f"Unable to find {target}")


def iterate_over_friends_object(friend):
    return friend["name"]

friends = [
    {"name": "a", "age": 1},
    {"name": "b", "age": 2},
    {"name": "c", "age": 3},
]

print(search(friends, "c", iterate_over_friends_object))