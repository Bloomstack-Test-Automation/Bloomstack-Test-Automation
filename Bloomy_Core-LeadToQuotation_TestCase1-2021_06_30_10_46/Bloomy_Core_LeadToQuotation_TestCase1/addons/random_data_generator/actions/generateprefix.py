"""This module contains the GeneratePrefix proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GeneratePrefix(ActionProxy):
    def __init__(self):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="-kT4Fi1xFk6PF8xkHU4vDg",
            classname="GeneratePrefix"
        )
        self.result = None
