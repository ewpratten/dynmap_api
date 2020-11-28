import requests

from ..datastructures.worldupdate import WorldUpdate

def fetchServerUpdate(dynmap_url: str, world: str) -> WorldUpdate:

    # Make remote request
    response = requests.get(f"{dynmap_url}/up/world/{world}/0")

    # Deserialize contents
    return WorldUpdate(**response.json())

