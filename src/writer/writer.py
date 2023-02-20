import abc
from typing import Any, Callable


def writer_interceptor(func: Callable[[Any, Any], Any]) -> Callable[[Any, Any], Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("--Writer Start--")
        result: Any = func(*args, **kwargs)
        print("--Writer End--")
        return result

    return wrapper


class IWriter(metaclass=abc.ABCMeta):
    def write(self, item: Any) -> None:
        raise NotImplementedError()
