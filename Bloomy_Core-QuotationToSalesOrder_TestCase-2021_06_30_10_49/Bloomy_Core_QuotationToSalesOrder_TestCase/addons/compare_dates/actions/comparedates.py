"""This module contains the CompareDates proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class CompareDates(ActionProxy):
    def __init__(self, dateOne: str, dateTwo: str, format: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="MSHCupRETUmZoTYn1n4kiw",
            classname="CompareDates"
        )
        self.dateOne = dateOne
        self.dateTwo = dateTwo
        self.format = format
        self.result = None
