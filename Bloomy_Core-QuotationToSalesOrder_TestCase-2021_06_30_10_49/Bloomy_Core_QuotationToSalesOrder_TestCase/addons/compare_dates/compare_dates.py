from .actions import CompareDates


class CompareDates:
    @staticmethod
    def comparedates(dateOne: str, dateTwo: str, format: str) -> CompareDates:
        """Compare {{dateOne}} with {{dateTwo}}."""
        return CompareDates(dateOne, dateTwo, format)
