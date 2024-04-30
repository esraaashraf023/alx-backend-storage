#!/usr/bin/env python3
"""tasks"""


import redis
from uuid import uuid4
from functools import wraps
from typing import Any, Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """1, 2, 3"""

    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """Wraps called method"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper
