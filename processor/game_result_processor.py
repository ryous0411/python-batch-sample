from entity.game_result import GameResult
from game_result import GameResult as EnumGameResult
from processor.processor import IProcessor, processor_interceptor


class GameResultProcessor(IProcessor):

    @processor_interceptor
    def process(self, items: list[GameResult]):
        max_score: int = max(list(map(lambda x: x.score, items)))

        return list(map(
            lambda i: self._create_game_result(i, max_score), items
        ))

    @staticmethod
    def _create_game_result(game_result: GameResult, max_score: int) -> GameResult:
        result: EnumGameResult = EnumGameResult.WIN if game_result.is_won(max_score) else EnumGameResult.LOSE

        return GameResult(
            user_id=game_result.user_id,
            title=game_result.title,
            score=game_result.score,
            result=result.value
        )
