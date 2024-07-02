"""_summary_

Returns:
    _type_: _description_
"""
from typing import Any, Hashable


__all__ = ["search"]


def search(data_list: list[dict], key: Hashable, val: Any) -> list[dict]:
    res = []

    for item in data_list:
        if item.get(key) == val:
            res.append(item)

    return res
