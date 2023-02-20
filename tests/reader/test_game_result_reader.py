from typing import List
from unittest.mock import patch, MagicMock

from src.entity.game_result import GameResult
from src.game_result import GameResult as EnumGameResult
from src.game_title import GameTitle
from src.reader.game_result_reader import GameResultReader


class TestGameResultReader(GameResultReader):

    @patch("src.reader.game_result_reader.GameResultRepository.find_all_by_title")
    def test_should_read_game_result(self, find_all_by_title: MagicMock) -> None:
        find_all_by_title.return_value = [
            GameResult(
                user_id="1",
                title=GameTitle.GALAXY_INVADERS.value,
                score=50,
                result=EnumGameResult.WIN.value
            )
        ]
        args: List[str] = [GameResultReader.__class__.__name__, GameTitle.GALAXY_INVADERS.value]
        results: List[GameResult] = self.read(args)

        assert len(results) == 1

        result: GameResult = results[0]

        assert result.user_id == "1"
        assert result.title == GameTitle.GALAXY_INVADERS.value
        assert result.score == 50
        assert result.result == EnumGameResult.WIN.value
