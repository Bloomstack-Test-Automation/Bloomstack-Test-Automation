"""This module contains the GenerateNumberInRange proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GenerateNumberInRange(ActionProxy):
    def __init__(self, min: str, max: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="-kT4Fi1xFk6PF8xkHU4vDg",
            classname="GenerateNumberInRange"
        )
        self.min = min
        self.max = max
        self.result = None
