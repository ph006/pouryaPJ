"""_summary_

Returns:
    _type_: _description_
"""

from typing import Any, Hashable, Iterable
from os import system


__all__ = ["get_input", "show_list_dict"]


def get_input(filed: str, is_empty: bool = True, valid_range: Iterable = ()) -> str:

    err_list = []

    while True:
        val = input(f"{filed} : ")
        system("cls")

        if not is_empty and val == "":
            err_list.append(f"value is empty!!!")

        if valid_range and val not in valid_range:
            err_list.append(f"value not in valid range!!!")

        if not err_list:
            return val

        print(*err_list, sep="\n")
        err_list.clear()


def show_list_dict(data_list: list[dict], *keys: Hashable, word_len=20, is_capital=False, display_row=False) -> None:

    if display_row:
        print("row".ljust(5), end="")

    for key in keys:
        print(f"{key.ljust(word_len)}", end="")

    print("\n", "-"*(len(keys)*word_len), sep="")

    for row_num, item in enumerate(data_list, 1):

        if display_row:
            print(str(row_num).ljust(5), end="")

        for key in keys:
            print(f"{(str(item.get(key)).capitalize()
                  if is_capital else item.get(key)).ljust(word_len)}", end="")

        print()

    print("-"*(len(keys)*word_len))
