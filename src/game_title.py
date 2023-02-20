from enum import Enum
from typing import List


class GameTitle(Enum):
    GALAXY_INVADERS = "galaxy_invaders"
    METEOR_BLASTERS = "meteor_blasters"
    STARSHIP_X = "starship_x"

    @classmethod
    def values(cls) -> List[str]:
        return [v.value for v in GameTitle]

    @classmethod
    def exists(cls, title: str) -> bool:
        return title in cls.values()
