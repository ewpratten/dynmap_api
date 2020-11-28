
from typing import List

# Data
from ..datastructures.configuration import ClientConfiguration
from ..datastructures.worldupdate import WorldUpdate

# API calls
from .configuration import fetchRemoteConfig
from .worldupdate import fetchServerUpdate


class DynmapConnectionContext(object):
    """An object-oriented interface for interacting with a Dynmap server"""

    config: ClientConfiguration
    _baseurl: str

    def __init__(self, baseurl: str):
        self._baseurl = baseurl

        # Fetch configuration
        self.config = fetchRemoteConfig(baseurl)

    def getWorldUpdate(self, world: str) -> WorldUpdate:
        
        # Handle invalid world
        for valid_world in self.config.worlds:
            if valid_world.name == world:
                break
        else:
            return None
        
        # Return data
        return fetchServerUpdate(self._baseurl, world)
    
    
        
