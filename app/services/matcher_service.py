from dataclasses import dataclass
from typing import Optional


@dataclass
class SearchIntent:
    """
    Represents the parsed intent from a user's natural language query.

    Example:
        Query:
            "Find Login button"

        Parsed Intent:
            search_text = "login"
            element_type = "button"
    """

    # Original query entered by the user
    raw_query: str

    # Text used to identify the element
    search_text: str = ""

    # Expected UI element type
    element_type: Optional[str] = None

    # Optional position
    # Example:
    # "second button"
    index: Optional[int] = None

    # Future use
    section: Optional[str] = None

    # Matching confidence
    confidence: int = 0

    def __str__(self) -> str:
        return (
            f"SearchIntent("
            f"search_text='{self.search_text}', "
            f"element_type='{self.element_type}', "
            f"index={self.index})"
        )