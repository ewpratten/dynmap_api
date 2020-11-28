from pydantic import BaseModel
from typing import List

class Map(BaseModel):
    
    inclination: int
    nightandday: bool
    image_format: str
    shader: str
    compassview: str
    prefix: str
    icon: str
    scale: int
    azimuth: int
    type: str
    title: str
    lighting: str
    backgroundday: str
    bigmap: bool
    maptoworld: List[int]
    worldtomap: List[int]
    protected: bool
    background: str
    mapzoomout: int
    boostzoom: int
    name: str
    backgroundnight: str
    perspective: str
    mapzoomin: int
    