from itertools import groupby


def iterate(value: str) -> str:
    groups = groupby(value, lambda x: x)
    new_value = ""

    for k, group in groups:
        new_value += f"{len(list(group))}{k}"

    return new_value
