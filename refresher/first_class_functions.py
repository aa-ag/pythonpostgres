def search(sequence, target, search_method):
    for i in sequence:
        if search_method(i) == target:
            return f"Yes, {i} is found in provided sequence"
    raise RuntimeError(f"Unable to find {target}")
