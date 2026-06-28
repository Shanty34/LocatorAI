from app.services.browser_service import BrowserService
from app.services.parser_service import ParserService
from app.services.matcher_service import MatcherService
from app.services.locator_service import LocatorService

from app.models.context import LocatorContext


class LocatorEngine:

    def __init__(self):

        self.browser = BrowserService()

        self.parser = ParserService()

        self.matcher = MatcherService()

        self.locator = LocatorService()

    def find(self, url: str, query: str):

        context = LocatorContext(url=url)

        try:

            context = self.browser.open(context)
            context = self.parser.parse(context)

            context = self.matcher.match(
                query,
                context
            )
            context = self.locator.generate(
                context
            )

            return context

        finally:

            self.browser.close()