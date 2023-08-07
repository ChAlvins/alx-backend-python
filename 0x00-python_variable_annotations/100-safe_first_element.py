#!/usr/bin/env python3
"""safe_first_element method"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns first element of a seqeunce if existing"""
    if lst:
        return lst[0]
    else:
        return None
