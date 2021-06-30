from .actions import MultiClicker


class ClicksMultiplier:
    @staticmethod
    def multiclicker(amount: str, delay: int, javascript: str) -> MultiClicker:
        """Perform needed amount of click on element."""
        return MultiClicker(amount, delay, javascript)
