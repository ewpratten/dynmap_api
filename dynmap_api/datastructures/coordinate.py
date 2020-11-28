from pydantic import BaseModel


class Coordinate(BaseModel):
    """Represents a Minecraft coordinate"""

    x: int
    y: int
    z: int
