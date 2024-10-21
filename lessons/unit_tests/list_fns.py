def get_first(a_list: list[str]) -> str:
    return a_list[0]


def remove_first(a_list: list[str]) -> None:
    a_list.pop(0)


def get_and_remove_first(a_list: list[str]) -> str:
    first = get_first(a_list=a_list)
    remove_first(a_list=a_list)
    return first
