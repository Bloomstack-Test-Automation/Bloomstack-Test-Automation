"""This module contains the GenerateLoremIpsum proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GenerateLoremIpsum(ActionProxy):
    def __init__(self):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="-kT4Fi1xFk6PF8xkHU4vDg",
            classname="GenerateLoremIpsum"
        )
        self.result = None
