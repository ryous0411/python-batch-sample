import abc
from typing import Any, Callable


def reader_interceptor(func: Callable[[Any, Any], Any]) -> Callable[[Any, Any], Any]:
    """

    :rtype: object
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("--Reader Start--")
        result: Any = func(*args, **kwargs)
        print("--Reader End--")
        return result

    return wrapper


class IReader(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def read(self, args: str) -> Any:
        raise NotImplementedError()
