import re


def resolve_table_name(name: str) -> str:
    names = re.split("(?=[A-Z])", name)
    return "_".join([x.lower() for x in names if x])
