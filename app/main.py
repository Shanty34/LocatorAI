from app.models.context import LocatorContext
from app.services.browser_service import BrowserService

context = LocatorContext(
    url="https://opensource-demo.orangehrmlive.com/"
)

browser = BrowserService()

context = browser.open(context)

print(context.title)

print(context.page.url)

print(context.page.locator("input").count())

browser.close()