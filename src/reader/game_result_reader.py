from typing import List, Any

from src.entity.game_result import GameResult
from src.game_title import GameTitle
from src.reader.reader import IReader, reader_interceptor
from src.repository.game_result_repository import GameResultRepository


class GameResultReader(IReader, GameResultRepository):

    @reader_interceptor
    def read(self, args: str) -> List[GameResult]:

        try:

            game_title: str = args[1]

            if not GameTitle.exists(game_title):
                raise GameTitleNotFoundError()

            return self.find_all_by_title(game_title)

        except IndexError as e:
            raise BatchArgsRequiredError(e)


class BatchArgsRequiredError(IndexError):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(args, kwargs)


class GameTitleNotFoundError(ValueError):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(args, kwargs)
