from dataclasses import dataclass, field
from typing import List, Optional

from playwright.sync_api import Browser, BrowserContext, Page

from app.models.element import Element
from app.models.locator import Locator


@dataclass
class LocatorContext:
    """
    Holds all runtime information for a locator search session.
    """
    # User input
    url: str

    # Browser objects
    browser: Optional[Browser] = None
    browser_context: Optional[BrowserContext] = None
    page: Optional[Page] = None

    # Page metadata
    title: str = ""

    # Parsed data
    elements: List[Element] = field(default_factory=list)

    # Search result
    matched_element: Optional[Element] = None

    # Generated locators
    generated_locators: List[Locator] = field(default_factory=list)

    # Optional debug information
    debug_messages: List[str] = field(default_factory=list)

    def log(self, message: str):
        """
        Store debug messages during execution.
        """
        self.debug_messages.append(message)