from playwright.sync_api import sync_playwright

from app.models.context import LocatorContext
from app.models.browser_config import BrowserConfig


class BrowserService:

    def __init__(self, config: BrowserConfig | None = None):

        self.config = config or BrowserConfig()

        self.playwright = None
        self.browser = None

    def open(self, context: LocatorContext) -> LocatorContext:

        context.log("Starting Playwright...")

        self.playwright = sync_playwright().start()

        browser_type = getattr(
            self.playwright,
            self.config.browser
        )

        self.browser = browser_type.launch(
            headless=self.config.headless,
            slow_mo=self.config.slow_mo
        )

        browser_context = self.browser.new_context(
            viewport={
                "width": self.config.viewport_width,
                "height": self.config.viewport_height
            },
            user_agent=self.config.user_agent
        )

        page = browser_context.new_page()

        page.set_default_timeout(
            self.config.timeout
        )

        context.log(f"Navigating to {context.url}")

        page.goto(
            context.url,
            wait_until="networkidle"
        )

        context.browser = self.browser
        context.browser_context = browser_context
        context.page = page
        context.title = page.title()

        context.log(f"Loaded '{context.title}'")

        return context

    def close(self):

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()