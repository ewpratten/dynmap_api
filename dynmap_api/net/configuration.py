import requests

from ..datastructures.configuration import ClientConfiguration


def fetchRemoteConfig(dynmap_url: str) -> ClientConfiguration:
    """Fetch configuration information from a dynmap server

    Args:
        dynmap_url (str): Dynmap API base URL

    Returns:
        ClientConfiguration: Configuration object
    """

    # Make request
    response = requests.get(f"{dynmap_url}/up/configuration")

    # Deserialize
    return ClientConfiguration(**response.json())
