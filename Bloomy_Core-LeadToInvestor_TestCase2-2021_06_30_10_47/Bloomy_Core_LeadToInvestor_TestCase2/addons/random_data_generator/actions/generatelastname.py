"""This module contains the GenerateLastName proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GenerateLastName(ActionProxy):
    def __init__(self):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="-kT4Fi1xFk6PF8xkHU4vDg",
            classname="GenerateLastName"
        )
        self.result = None
