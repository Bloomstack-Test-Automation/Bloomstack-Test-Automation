"""This module contains the FindLastSubstringIndexFromIndex proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class FindLastSubstringIndexFromIndex(ActionProxy):
    def __init__(self, sourceString: str, subString: str, fromIndex: int):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="FindLastSubstringIndexFromIndex"
        )
        self.sourceString = sourceString
        self.subString = subString
        self.fromIndex = fromIndex
        self.index = None
