from entity.game_result import GameResult
from repository.game_result_repository import GameResultRepository
from writer.writer import IWriter, writer_interceptor


class GameResultWriter(IWriter, GameResultRepository):
    @writer_interceptor
    def write(self, item: list[GameResult]) -> None:
        for game_result in item:
            self.upsert(game_result)
