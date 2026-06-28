from dataclasses import dataclass


@dataclass
class Locator:
    """
    Represents one locator strategy for an element.
    """

    strategy: str

    value: str

    confidence: int

    recommended: bool = False

    framework: str = "Generic"

    reason: str = ""

    def __str__(self):

        star = "⭐" if self.recommended else " "

        return (
            f"{star} "
            f"[{self.strategy}] "
            f"{self.value} "
            f"({self.confidence}%)"
        )