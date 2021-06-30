from .actions import FuturePastAction


class GenerateDateTimeCurrentFutureOrPast:
    @staticmethod
    def futurepastaction(days: int, months: int, years: int, hours: int, minutes: int, format: str) -> FuturePastAction:
        """Positive values for future and negative for past dates."""
        return FuturePastAction(days, months, years, hours, minutes, format)
