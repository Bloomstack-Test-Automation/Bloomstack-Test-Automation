"""This module contains the GenerateSyllable proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GenerateSyllable(ActionProxy):
    def __init__(self):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="-kT4Fi1xFk6PF8xkHU4vDg",
            classname="GenerateSyllable"
        )
        self.result = None
