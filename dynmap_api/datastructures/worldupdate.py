from pydantic import BaseModel
from typing import List

from .player import Player

class WorldUpdate(BaseModel):
    currentcount: int
    servertime: int
    timestamp: int
    players: List[Player]