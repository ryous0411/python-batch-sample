import abc
from typing import Any


def reader_interceptor(func):
    def wrapper(*args, **kwargs):
        print("--Reader Start--")
        result: Any = func(*args, **kwargs)
        print("--Reader End--")
        return result

    return wrapper


class IReader(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def read(self, args) -> Any:
        raise NotImplementedError()
