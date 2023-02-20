from typing import Any, Callable

from src.processor.processor import IProcessor
from src.reader.reader import IReader
from src.writer.writer import IWriter


def batch_interceptor(func: Callable[[Any, Any], Any]) -> Callable[[Any, Any], Any]:
    def wrapper(*args: Any, **kwargs: Any) -> None:
        print("--Batch Start--")
        func(*args, **kwargs)
        print("--Batch End--")

    return wrapper


class Batch:

    def __init__(self, reader: IReader, processor: IProcessor, writer: IWriter):
        self._reader = reader
        self._processor = processor
        self._writer = writer

    @batch_interceptor
    def execute(self, *args: str) -> None:
        extracted_item: Any = self._reader.read(*args)
        processed_item: Any = self._processor.process(extracted_item)
        self._writer.write(processed_item)
