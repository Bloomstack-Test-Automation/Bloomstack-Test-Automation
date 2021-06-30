"""This module contains the FuturePastAction proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class FuturePastAction(ActionProxy):
    def __init__(self, days: int, months: int, years: int, hours: int, minutes: int, format: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="02zAWIC7IUym1Rp8eFfaCg",
            classname="FuturePastAction"
        )
        self.days = days
        self.months = months
        self.years = years
        self.hours = hours
        self.minutes = minutes
        self.format = format
        self.date = None
        self.futureDateInMilliSeconds = None
