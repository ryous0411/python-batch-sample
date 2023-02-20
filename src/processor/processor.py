import abc
from typing import Any, Callable


def processor_interceptor(func: Callable[[Any, Any], Any]) -> Callable[[Any, Any], Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("--Processor Start--")
        result: Any = func(*args, **kwargs)
        print("--Processor End--")
        return result

    return wrapper


class IProcessor(metaclass=abc.ABCMeta):

    def process(self, item: Any) -> Any:
        raise NotImplementedError()
