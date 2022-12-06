from itertools import groupby


def iterate(value: str) -> str:
    groups = groupby(value, lambda x: x)
    new_value = ""

    for k, group in groups:
        new_value += f"{len(list(group))}{k}"

    return new_value


def example(data: str):
    for i in range(0, 50):
        data = iterate(data)

    found = len(data)

    if not found:
        raise ValueError()

    return found
