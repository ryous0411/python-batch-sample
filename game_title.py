from strenum import StrEnum


class GameTitle(StrEnum):
    GALAXY_INVADERS = "galaxy_invaders"
    METEOR_BLASTERS = "meteor_blasters"
    STARSHIP_X = "starship_x"

    @classmethod
    def values(cls) -> list:
        return list(map(lambda c: c.value, cls))

    @classmethod
    def exists(cls, title: str) -> bool:
        return title in cls.values()
