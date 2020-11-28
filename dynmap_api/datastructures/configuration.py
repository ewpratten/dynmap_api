from pydantic import BaseModel
from typing import List

from .world import World


class ClientConfiguration(BaseModel):
    """Represents configuration data sent by dynmap backend on connection"""

    updaterate: int
    chatlengthlimit: int
    confighash: int
    defaultmap: str
    title: str
    defaultzoom: int
    allowwebchat: bool
    allowchat: bool
    webchat_interval: int
    loggedin: bool
    coreversion: str
    webchat_requires_login: bool
    login_enabled: bool
    maxcount: int
    dynmapversion: str
    cyrillic: bool
    webprefix: str
    defaultworld: str

    worlds: List[World]
    components: List[dict]
