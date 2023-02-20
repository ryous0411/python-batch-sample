import abc
from typing import List, Dict, Any

from src.entity.game_result import GameResult
from src.infra.dynamodb.game_result_driver import GameResultDriver


class IGameResultRepository(metaclass=abc.ABCMeta):

    def find_all_by_title(self, title: str) -> list[GameResult]:
        raise NotImplementedError()

    def upsert(self, game_result: GameResult) -> None:
        raise NotImplementedError()


class GameResultRepository(IGameResultRepository, GameResultDriver):

    def find_all_by_title(self, title: str) -> List[GameResult]:
        game_scores: List[Dict[str, Any]] = self.query_by_title(title)

        return list(
            map(lambda x: GameResult(
                user_id=x["user_id"]["S"],
                title=x["title"]["S"],
                score=int(x["score"]["N"]),
                result=x["result"]["S"] if x.get("result", None) else None
            ), game_scores)
        )

    def upsert(self, game_result: GameResult) -> None:
        item: Dict[str, Any] = {
            "user_id": {"S": game_result.user_id},
            "title": {"S": game_result.title},
            "score": {"N": str(game_result.score)},
            "result": {"S": game_result.result}
        }

        self.put_game_result(item)
