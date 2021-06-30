"""This module contains the MultiClicker proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class MultiClicker(ActionProxy):
    def __init__(self, amount: str = "1", delay: int = 200, javascript: str = "false"):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="1k0K_tDT5UqVDY42xr4kPw",
            classname="io.testproject.MultiClicker"
        )
        self.amount = amount
        self.javascript = javascript
        self.delay = delay
