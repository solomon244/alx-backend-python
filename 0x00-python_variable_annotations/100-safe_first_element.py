#!/usr/bin/env python3
"""
safe_first_element
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Reterive elment fron the sequence object or None """
    if lst:
        return lst[0]
    else:
        return None
