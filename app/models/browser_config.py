from dataclasses import dataclass


@dataclass
class BrowserConfig:
    """
    Configuration for Playwright browser.
    """

    browser: str = "chromium"

    headless: bool = True

    timeout: int = 30000

    slow_mo: int = 0

    viewport_width: int = 1440

    viewport_height: int = 900

    user_agent: str | None = None