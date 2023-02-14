import abc
from typing import Any


def writer_interceptor(func):
    def wrapper(*args, **kwargs):
        print("--Writer Start--")
        result: Any = func(*args, **kwargs)
        print("--Writer End--")
        return result

    return wrapper


class IWriter(metaclass=abc.ABCMeta):
    def write(self, item: Any):
        raise NotImplementedError()
