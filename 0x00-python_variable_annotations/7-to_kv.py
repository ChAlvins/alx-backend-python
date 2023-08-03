#!/usr/bin/env python3
"""contains annotated to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returning a tuple of key and square of its value"""
    return (k, v**2)
