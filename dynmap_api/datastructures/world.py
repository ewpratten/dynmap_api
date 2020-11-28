from pydantic import BaseModel
from typing import List

from .coordinate import Coordinate
from .map import Map


class World(BaseModel):

    sealevel: int
    protected: bool
    extrazoomout: int
    center: Coordinate
    name: str
    title: str
    worldheight: int
    maps: List[Map]
