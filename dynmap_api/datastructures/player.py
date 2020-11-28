from pydantic import BaseModel

from .coordinate import Coordinate


class Player(BaseModel):
    """Represents a Minecraft player"""

    world: str
    name: str
    account: str
    x: int
    y: int
    z: int
    armor: int
    health: int
    sort: int
    type: str

    def isInHiddenWorld(self) -> bool:
        return self.world == "-some-other-bogus-world-"

    def getCoordinate(self) -> Coordinate:
        return Coordinate(**{
            "x": self.x,
            "y": self.y,
            "z": self.z,
        })
