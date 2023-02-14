class GameResult:

    def __init__(self, user_id: str, title: str, score: int, result: str):
        self._user_id = user_id
        self._title = title
        self._score = score
        self._result = result

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def score(self) -> int:
        return self._score

    @property
    def result(self) -> str:
        return self._result

    def is_won(self, max_score: int):
        return True if self._score == max_score else False
