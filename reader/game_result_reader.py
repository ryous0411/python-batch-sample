from entity.game_result import GameResult
from game_title import GameTitle
from reader.reader import IReader, reader_interceptor
from repository.game_result_repository import GameResultRepository


class GameResultReader(IReader, GameResultRepository):

    @reader_interceptor
    def read(self, args) -> list[GameResult]:

        try:

            game_title = args[1]

            if not GameTitle.exists(game_title):
                raise GameTitleNotFoundError()

            return self.find_all_by_title(game_title)

        except IndexError as e:
            raise BatchArgsRequiredError(e)


class BatchArgsRequiredError(IndexError):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class GameTitleNotFoundError(ValueError):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
