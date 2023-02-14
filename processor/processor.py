import abc
from typing import Any


def processor_interceptor(func):
    def wrapper(*args, **kwargs):
        print("--Processor Start--")
        result: Any = func(*args, **kwargs)
        print("--Processor End--")
        return result

    return wrapper


class IProcessor(metaclass=abc.ABCMeta):

    def process(self, item: Any):
        raise NotImplementedError()
