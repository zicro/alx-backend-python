#!/usr/bin/env python3
"""duck typed annotations"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retrieve first el of sequence"""
    if lst:
        return lst[0]
    else:
        return None
